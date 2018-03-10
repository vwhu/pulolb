import pandas as pd
import numpy as np
import import_data
import sort_data
from tqdm import tqdm_notebook as tqdm
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw


def curve_distance(a, b):
    """This function calculates the time warping distance between two curves.
    Inputs are two NumPy arrays
    """

    distance, path = fastdtw(a, b, dist=euclidean)
    return distance


def distance_cycle_to_full(cycle,dic1,dic2):
    """This function calculates the time warping distance between a partial curve and full curves 
    Inputs are two dictionaries and a key number to identify the curve
    """

    if cycle not in dic1.keys():
        pass
    else:
        
        # Get the range of voltages for the curve under evaluation.  
        a = dic1[cycle][['voltage']].values.flatten()
        a_max = a.max()
        a_min = a.min()
        a = a[1::2]
        
        Y = []
        
        # Calculate distance between the curve under evaluation and all the full curves
        for idx in tqdm(dic2.keys()):
            if idx in dic2.keys():
                b = dic2[idx][['voltage']].values.flatten()
                if len(b) > 100:  
                    # Create a filter so that we are only looking at values within the partial curve voltage range
                    b = dic2[idx][['voltage']].values.flatten()
                    b_max = np.argwhere(b < a_max)[0][0]
                    b_min = np.argwhere(b > a_min)[-1][0]
                    b = b[int(b_max):int(b_min)]
                    
                    d = curve_distance(a,b)
            
                    A = [idx,d]
                    Y.append(A)
                else:
                    pass
            else:
                pass
    # Creat a DataFrame with the information, sorted by distance            
    df = pd.DataFrame(Y, columns = ['Cycle','Distance'])
    df = df.sort_values(by = ['Distance'])
    
    return df

def partial_to_full(dic1,dic2):
    """This function relates partial curves to full curves, according to the distances between them
    The inputs are two dictionaries"""
    C = []
    D = []
    F = []
    
    # Calculate the closest full curve for all the partial curves under evaluation
    for i in tqdm(dic1.keys()):
        df = distance_cycle_to_full(i,dic1,dic2)
        Distance = df['Distance'][df.index[0]]
        Full_cycle = df['Cycle'][df.index[0]]
        C.append(i)
        D.append(Distance)
        F.append(Full_cycle)
       
    D = np.array(D)
    C = np.array(C)
    F = np.array(F)
    return D,C,F

def get_lifetime(dic1,dic2,cap):
    """This function calculates the parameters needed to diagnose the battery
    The inputs are two dictionaries and the original capacity of the battery tested.
    """
    
    # Get the full curve related to each of the partial curves tested
    D,C,F = partial_to_full(dic1,dic2)

    
    Capacity = []
    Percent = []
    Time = []
    Slope = []
    Intercept = []
    Life = []
    
    # For each curve tested, get the parameters
    for i in range(1,len(F)-1):
        idx = dic2[F[i]].shape[0]
        # Capacity remaining
        capacity = dic2[F[i]]['discharge_ah'][dic2[F[i]].index[idx-1]] - dic2[F[i]]['discharge_ah'][dic2[F[i]].index[0]]
        percent = ((capacity)/cap)*100 
        # Usage time
        time = dic1[C[i]]['time'][dic1[C[i]].index[dic1[C[i]].shape[0]-1]]
                                                           
        # Coeff. for linear regression between capacity and time
        coeff = np.polyfit([float(0),time],[float(100),percent],1)
        # Failure time
        life = -coeff[1]/coeff[0]
        
        Capacity.append(capacity)
        Percent.append(percent)
        Time.append(time)
        Slope.append(coeff[0])
        Intercept.append(coeff[1])
        Life.append(life)
    
    return Percent, Time, Slope, Intercept, Life

def life_plot(time,slope,intercept,percent,life):
    """This function calculates the parameters needed to diagnose the battery
    The inputs are the usage time, slope and intercept for regression between time and capacity
    and the actual capacity
    """

    # Plot the prediction for the battery life
    fig = plt.figure(figsize = (8, 6))
    x = [time/(3600*24*7),life/(3600*24*7)]
    y = [time*slope + intercept, life*slope + intercept]
    
    x1 = [0,time/(3600*24*7)]
    y1 = [intercept, time*slope + intercept]
   
    plt.plot(x1,y1)
    plt.scatter(time/(3600*24*7),percent)
    plt.plot(x,y,ls = '--')
    plt.ylim(0, 100)
    plt.xlim(0, life/(3600*24*7))
    plt.title('Life prediction')
    plt.xlabel('Time (weeks)')
    plt.ylabel('Remaining Capacity (%)')
    return 

