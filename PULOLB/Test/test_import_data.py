import sort_data
import import_data
import pandas as pd
filename = 'converted_PL03.mat'
df = import_data.single_pd_matlab_data(filename)
def test_single_mat_file():
    #File format test
    if filename.endswith('.mat'):
        pass
    else:
        raise TypeError('Filename not in .mat')
    
    #Check if Cycle number is monotonically increasing
    #By Checking monotonicity, we know the uniformity of our data
    if df['cycle'].is_monotonic_increasing == True:
        pass
    else:
        raise Exception('Cycle number is not correctly stored in the dataframe')

    #Check if the time series is monotonically increasing and print out the abnormal values 
    #as well as the location in our dataframe
    if df.time.is_monotonic_increasing == True:
        pass
    else:   
        a = df.time.values.flatten()
        a_list = []
        for x,y in zip(a,a[1:]):
            if x > y:
                print('Problematic datetime:',x,y)
                a_list.append(x)
            else:
                pass
    #If the number of noise points in the list is greater than 10 (we can set any value), an exception is raised
    if len(a_list) > 10:
        raise ValueError('Our time data is not fully cleaned')
    
    #Check if the datetime series is monotonically increasing
    if df.datetime.is_monotonic_increasing == True:
        pass
    else:   
        b = df.datetime.values.flatten()
        a_list = []
        for x,y in zip(b,b[1:]):
            if x > y:
                print('Problematic datetime:' ,x, y)
                a_list.append(x)
                print(df.loc[df['datetime'] == x])
            else:
                pass    

    if len(a_list) > 10:
        raise ValueError('Our datetime data is not fully cleaned')

    #Check the uniformity in our voltage data, we can define a difference of 0.5 between two voltage as the threshold
    c = df['voltage']
    count = 0
    a_list = []
    for x,y in zip(c,c[1:]):
        count = count + 1
        if abs(x-y)>0.5:
            a_list.append(x)
            #Print the two rows with big voltage difference
            print(df.loc[count-1],df.loc[count-1])
        else:
            pass

    if len(a_list) > 10:
        raise ValueError('Our voltage data is not fully cleaned')
