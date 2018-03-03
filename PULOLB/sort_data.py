import pandas as pd
import import_data

def by_cycle(filename):
    """This function sorts the data by the cycle number"""
    
    df = import_data.single_pd_matlab_data(filename)
    
    #Initialize a dictionary for the cycle number
    cycle_dict = {}
    cycle_list = df['cycle'].unique()

    #Add the data in the dictonary so that the keys are the cycle numbers
    for idx in list(cycle_list):
        if idx not in cycle_dict.keys():
            cycle_dict[idx] = df.loc[df['cycle'] == idx]
        else:
            pass
    
    return cycle_dict    

def charge_discharge(filename):
    """This function separates the data into charge and discharge cycles"""
    
    #Creat the data dictionary sorted by cycle number
    cycle_dict = by_cycle(filename)
    
    #Initialize dictionaries for charge and discharge
    charge_dict = {}
    discharge_dict = {}
    
    #Add the data into the dictionaries
    for idx in list(cycle_dict.keys()):
        if idx not in charge_dict.keys():
            charge_dict[idx] = cycle_dict[idx].loc[cycle_dict[idx]['current_amp'] > 0]
            discharge_dict[idx] = cycle_dict[idx].loc[cycle_dict[idx]['current_amp'] < 0]
        else:
            pass
        
    return charge_dict, discharge_dict