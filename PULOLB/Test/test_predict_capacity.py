import predict_capacity
import pandas as pd
import numpy as np
filename_partial = 'converted_PL03.mat'
filename_full = 'converted_PL11.mat'

charge_partial, discharge_partial = predict_capacity.sort_data.charge_discharge(
    filename_partial)
charge_full, discharge_full = predict_capacity.sort_data.charge_discharge(
    filename_full)

# Make short dictionaries for testing purpose
PL03d_short = {}
for idx in range(1, len(discharge_partial.keys()), 50):
    if idx in discharge_partial.keys():
        if idx not in PL03d_short.keys():
            PL03d_short[idx] = discharge_partial[idx]

full_curvesd_short = {}
for idx in range(1, len(discharge_full.keys()), 50):
    if idx in discharge_full.keys():
        if idx not in full_curvesd_short.keys():
            full_curvesd_short[idx] = discharge_full[idx]


def test_curve_distance():
    
    b = PL03d_short[1][['voltage']].values.flatten()
    # Check input array type
    if isinstance(b, np.ndarray):
        pass
    else:
        raise TypeError('Input must be a numpy array')


def test_distance_cycle_to_full():
    
    df = predict_capacity.distance_cycle_to_full(
        1, PL03d_short, full_curvesd_short)
    # Check if the returned dataframe is sorted in terms of distance
    df2 = df.sort_values(by=['Distance'])
    if df.equals(df):
        pass
    else:
        raise ValueError('The dataframe is not sorted')

    # Check the length of the columns
    if len(df.columns) == 2:
        pass
    else:
        raise Exception('There should be two columns: distance and cycle')

    # Check the length of the returned df
    if len(df) != len(full_curvesd_short.keys()):
        raise Exception(
            'The number of the keys in the full cycle dict should match with the length of the returned dataframe')
    else:
        pass


def test_partial_to_full():
    
    D, C, F = predict_capacity.partial_to_full(PL03d_short, full_curvesd_short)
    # Make sure the number of partial discharge keys are the same with the
    # list length
    if len(C) == len(PL03d_short.keys()):
        pass
    else:
        raise Exception(
            'Number of keys in partial dict is unmatched with the list length')

    # Make sure the length of distance dict and cycle dict are the same
    if len(D) == len(F):
        pass
    else:
        raise Exception(
            'The length of distance dict and cycle dict dont match')


def test_get_lifetime():
    Percent, Time, Slope, Intercept, Life = predict_capacity.get_lifetime(
        PL03d_short, full_curvesd_short, 1.5)
    # We are not checking the full cycle dictionary because it is built from
    # our files and the data structure is known and well defined.

    # User input dict check
    # Check the input data type
    if (isinstance(PL03d_short, dict)) & (
            isinstance(full_curvesd_short, dict)):
        pass
    else:
        raise TypeError('The input data should be two dicts')

    # Check the key value data type
    for i in PL03d_short.keys():
        if isinstance(PL03d_short[i], pd.DataFrame):
            pass
        else:
            raise TypeError('Each key value should be a pandas DataFrame')

    # Check the columns in the dataframe
    for i in PL03d_short.keys():
        if 'time' in PL03d_short[i].columns:
            pass
        else:
            raise Exception(
                'There should be a time(lowercase) column in the dataframe')

    for i in PL03d_short.keys():
        if 'voltage' in PL03d_short[i].columns:
            pass
        else:
            raise Exception(
                'There should be a voltage(lowercase) column in the dataframe')

    # Make sure the first input dictionary is the partial dict
    # All the voltages should be less than 4V
    for i in PL03d_short.keys():

        # Skip the first full cycle
        if i == 1:
            pass
        else:
            for x in PL03d_short[i]['voltage']:
                if x > 4:
                    raise ValueError(
                        'The partial discharge voltages should not be greater than 4V')
                else:
                    pass
    
    # Check the percentage, slope, and intercept
    for i in Percent:
        if i > 100:
            raise ValueError(
                'The percentage of a battery should not exceed 100%')
        else:
            pass
    for i in Slope:
        if i > 0:
            raise ValueError('The slope should be negative')
    for i in Intercept:
        if round(i) != 100:
            raise ValueError('The intercept should be 100%')
        else:
            pass
