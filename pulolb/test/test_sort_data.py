import sort_data
import pandas as pd
import import_data
filename = 'converted_PL04.mat'
cycle_dict = sort_data.by_cycle(filename)
charge, discharge = sort_data.charge_discharge(filename)


def test_cycle_sort():
    # File format test
    if filename.endswith('.mat'):
        pass
    else:
        raise TypeError('Filename not in .mat')
    df = import_data.single_pd_matlab_data(filename)

    # Dataframe column size test
    if len(df.columns) == 8:
        pass
    else:
        raise Exception('Wrong column numbers')

    # Voltage and time values test
    for i in cycle_dict.keys():
        for x in cycle_dict[i]['voltage']:
            if x < 0:
                print(cycle_dict[i].loc[cycle_dict[i]['voltage'] == x])
                raise ValueError('Voltage cant be negative')
    for t in cycle_dict[i]['time']:
        if t < 0:
                # Printing the row with negative values
            print(cycle_dict[i].loc[cycle_dict[i]['time'] == t])
            raise ValueError('Time cant be negative')


def test_charge_discharge():

    charge_ah_list = [0]
    discharge_ah_list = [0]
    # Charge_Ah test
    for i in charge.keys():
        for x in charge[i]['charge_ah']:
            if (x - charge_ah_list[-1]) < 0:
                print(charge[i].loc[charge[i]['charge_ah'] == x])
                raise Exception(
                    'Charge_ah shouldnt decrease in charging process')
            else:
                pass
    # Discharge_Ah test
    for i in discharge.keys():
        for x in discharge[i]['discharge_ah']:
            if (x - discharge_ah_list[-1]) < 0:
                print(charge[i].loc[charge[i]['discharge_ah'] == x])
                raise Exception(
                    'Discharge_ah shouldnt decrease in discharging process')
            else:
                pass

    # Voltage and time values test
    # Charge
    for i in charge.keys():
        for x in charge[i]['voltage']:
            if x < 0:
                print(charge[i].loc[charge[i]['voltage'] == x])
                raise ValueError('Voltage cant be negative')
    for t in charge[i]['time']:
        if t < 0:
                # Printing the row with negative values
            print(charge[i].loc[charge[i]['time'] == t])
            raise ValueError('Time cant be negative')
    # Discharge
    for i in discharge.keys():
        for x in discharge[i]['voltage']:
            if x < 0:
                print(discharge[i].loc[discharge[i]['voltage'] == x])
                raise ValueError('Voltage cant be negative')
    for t in discharge[i]['time']:
        if t < 0:
                # Printing the row with negative values
            print(discharge[i].loc[discharge[i]['time'] == t])
            raise ValueError('Time cant be negative')
