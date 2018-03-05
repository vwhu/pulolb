import hdf5storage
import numpy as np
import pandas as pd

def import_matlab_data(filename):
    """Taking a Matlab file of Arbin data from the CALCE database and imports it into a host of different NumPy arrays
    Filename: 
    The .mat file that needs to be converted to a pandas dataframe. """
    
    #Importing the file as a HDF5 dataframe, stored in the form of a dictionary.  
    df = hdf5storage.loadmat(filename)
    return df

def single_pd_matlab_data(filename):
	""" Unpacks the .mat data file for readibility as a pandas dataframe. 
	Filename: 
    The .mat file that needs to be converted to a pandas dataframe. """
    
    #Importing the file. 
    df = import_matlab_data(filename)
    keys = df.keys()

    #Changing the filename in the dictionary to data. 
    for i in keys:
            if i == '#subsystem#':
                pass
            else:
                data = i

    #Calling each column inside the file, and assigning column names. 
    time_sum = df['#subsystem#'][0][0][0][2][0][0].flatten()
    datetime_sum = df['#subsystem#'][0][0][0][2][0][1].flatten()
    step_sum = df['#subsystem#'][0][0][0][2][0][2].flatten()
    cycle_sum = df['#subsystem#'][0][0][0][2][0][3].flatten()
    current_sum = df['#subsystem#'][0][0][0][2][0][4].flatten()
    voltage_sum = df['#subsystem#'][0][0][0][2][0][5].flatten()
    charge_ah_sum = df['#subsystem#'][0][0][0][2][0][6].flatten()
    discharge_ah_sum = df['#subsystem#'][0][0][0][2][0][7].flatten()
    count = 9

 	#To access the number of cycles in each dataset. 
    for idx in range(1, len(df[data])): 
        #For missing data. 
        if df[data][idx][2].shape == (0,0):
            name = df[data][idx][0][0][0]
            name = name.split(' ')
            number = float(name[0])
            cycle_sum = np.append(cycle_sum, (cycle_sum[-1] + number)) 
        else:
        	#Concatenating all the data for one dataset with all the cycle operations for easy reference. 
            time_idx = (df['#subsystem#'][0][0][0][count][0][0].flatten()) + time_sum[-1]
            datetime_idx = df['#subsystem#'][0][0][0][count][0][1].flatten()
            

            step_idx = df['#subsystem#'][0][0][0][count][0][2].flatten()
            
            #To concatenate the cycle data, 
            if len(cycle_sum) > len(current_sum):
                diff = len(cycle_sum) - len(current_sum)
                cycle_prior = cycle_sum[-1]
                for i in range(0,diff):
                    cycle_sum = np.delete(cycle_sum, -1)
                cycle_idx = (df['#subsystem#'][0][0][0][count][0][3].flatten()) + cycle_prior
                cycle_test = (df['#subsystem#'][0][0][0][count][0][3].flatten())    
            else:
                cycle_prior = cycle_sum[-1]
                cycle_idx = (df['#subsystem#'][0][0][0][count][0][3].flatten()) + cycle_prior
                cycle_test = (df['#subsystem#'][0][0][0][count][0][3].flatten())              
            current_idx = df['#subsystem#'][0][0][0][count][0][4].flatten()
            voltage_idx = df['#subsystem#'][0][0][0][count][0][5].flatten()
            charge_ah_idx = df['#subsystem#'][0][0][0][count][0][6].flatten()
            discharge_ah_idx = df['#subsystem#'][0][0][0][count][0][7].flatten()

            min_ = np.unique(cycle_idx).min()
            max_ = np.unique(cycle_idx).max()
            idx_for_start = np.argwhere(cycle_idx == min_)[-1]
            idx_for_deletion = np.argwhere(cycle_idx == max_)[0]

            time_idx = time_idx[int(idx_for_start + 1):int(idx_for_deletion - 1)]
            datetime_idx = datetime_idx[int(idx_for_start + 1):int(idx_for_deletion - 1)]
            step_idx = step_idx[int(idx_for_start + 1):int(idx_for_deletion - 1)]
            cycle_idx = cycle_idx[int(idx_for_start + 1):int(idx_for_deletion - 1)]
            current_idx = current_idx[int(idx_for_start + 1):int(idx_for_deletion - 1)]
            voltage_idx = voltage_idx[int(idx_for_start + 1):int(idx_for_deletion - 1)]
            charge_ah_idx = charge_ah_idx[int(idx_for_start + 1):int(idx_for_deletion - 1)]
            discharge_ah_idx = discharge_ah_idx[int(idx_for_start + 1):int(idx_for_deletion - 1)]
        
            
            count = count + 7
            
            time_sum = np.concatenate((time_sum, time_idx), axis = 0)
            datetime_sum = np.concatenate((datetime_sum, datetime_idx), axis = 0)
            step_sum = np.concatenate((step_sum, step_idx), axis = 0)
            cycle_sum = np.concatenate((cycle_sum, cycle_idx), axis = 0)
            current_sum = np.concatenate((current_sum, current_idx), axis = 0)
            voltage_sum = np.concatenate((voltage_sum, voltage_idx), axis = 0)
            charge_ah_sum = np.concatenate((charge_ah_sum, charge_ah_idx), axis = 0)
            discharge_ah_sum = np.concatenate((discharge_ah_sum, discharge_ah_idx), axis = 0)
            if count > (len(df['#subsystem#'][0][0][0])-7):
                break

    host_df = pd.DataFrame()

    host_df['time'] = time_sum
    host_df['datetime'] = datetime_sum
    host_df['step'] = step_sum
    host_df['cycle'] = cycle_sum
    host_df['current_amp'] = current_sum
    host_df['voltage'] = voltage_sum
    host_df['charge_ah'] = charge_ah_sum
    host_df['discharge_ah'] = discharge_ah_sum
    
    return host_df
