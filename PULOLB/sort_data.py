import pandas as pd
import import_data

def by_cycle(filename):
    
    df = import_data.single_pd_matlab_data(filename)
    
    cycle_dict = {}
    cycle_list = df['cycle'].unique()

    for idx in list(cycle_list):
        if idx not in cycle_dict.keys():
            cycle_dict[idx] = df.loc[df['cycle'] == idx]
        else:
            pass
    
    return cycle_dict    

def charge_discharge(filename):
    
    cycle_dict = by_cycle(filename)
    
    charge_dict = {}
    discharge_dict = {}
    
    for idx in list(cycle_dict.keys()):
        if idx not in charge_dict.keys():
            charge_dict[idx] = cycle_dict[idx].loc[cycle_dict[idx]['current_amp'] > 0]
            discharge_dict[idx] = cycle_dict[idx].loc[cycle_dict[idx]['current_amp'] < 0]
        else:
            pass
        
    return charge_dict, discharge_dict