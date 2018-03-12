import hdf5storage
import numpy as np
import pandas as pd


def import_matlab_data(filename):
    """Taking a Matlab file of Arbin data from the CALCE database and imports it into a host of different NumPy arrays
        Filename: Matlab file
    """

    # Importing the file as a HDF5 dataframe, stored in the form of a
    # dictionary.
    df = hdf5storage.loadmat(filename)
    return df


def initialize_datasets(filename):
    """This function initializes the columns of the dataframe.
        Filename = matlab file
    """

    # Generate the dataframe
    df = import_matlab_data(filename)
    # Define a variable that contains the names of the dictionary's keys
    keys = df.keys()

    # Store the filename (second key in the dictionary) under the variable
    # call 'data'
    for i in keys:
        if i == '#subsystem#':
            pass
        else:
            data = i
    # To get the data out of the subsystem, start the count at 2
    count = 2

    for idx in range(1, len(df[data])):
        # Get the time column from the dataset (this gives the length of the
        # experiment)
        time_sum = df['#subsystem#'][0][0][0][count][0][0].flatten()

        # Evaluate the length of the experiment.
        # If it is a single cycle (less than 3500 data points), ignore it and
        # go to the next experiment
        if len(time_sum) < 3500:
            count = count + 7
        # If there are more cycles, initialize the names of the columns.
        else:
            datetime_sum = df['#subsystem#'][0][0][0][count][0][1].flatten()
            step_sum = df['#subsystem#'][0][0][0][count][0][2].flatten()
            cycle_sum = df['#subsystem#'][0][0][0][count][0][3].flatten()
            current_sum = df['#subsystem#'][0][0][0][count][0][4].flatten()
            voltage_sum = df['#subsystem#'][0][0][0][count][0][5].flatten()
            charge_ah_sum = df['#subsystem#'][0][0][0][count][0][6].flatten()
            discharge_ah_sum = df['#subsystem#'][0][0][0][count][0][7].flatten(
            )
            count = count + 7
            break

    return count, idx, time_sum, datetime_sum, step_sum, cycle_sum, current_sum, voltage_sum, charge_ah_sum, discharge_ah_sum


def single_pd_matlab_data(filename):
    """This function generates a dataframe with all the cycles included in the matlab file.
        Filename = matlab file
    """

    # Generate the dataframe
    df = import_matlab_data(filename)
    # Define a variable that contains the names of the dictionary's keys
    keys = df.keys()

    # Store the filename (second key in the dictionary) under the variable
    # call 'data'
    for i in keys:
        if i == '#subsystem#':
            pass
        else:
            data = i

    # Initialize the name of the columns
    count, idx, time_sum, datetime_sum, step_sum, cycle_sum, current_sum, voltage_sum, charge_ah_sum, discharge_ah_sum = initialize_datasets(
        filename)

    # Start the count from the 3rd row of the dataset
    start_ind = idx + 1

    for idx in range(int(start_ind), len(df[data])):
        # To access the number of cycles in each dataset.
        length_test = (df['#subsystem#'][0][0][0][count][0][0].flatten())

        # For missing data: Store the number of cycles with missing data and
        # add them up into the cycles count
        if df[data][idx][2].shape == (0, 0):
            name = df[data][idx][0][0][0]
            name = name.split(' ')
            number = float(name[0])
            cycle_sum = np.append(cycle_sum, (cycle_sum[-1] + number))

        # For single cycles: Ignore cycles with less than 3500 values.
        elif len(length_test) < 3500:
            count = count + 7
        # Extract data from each column
        else:
            time_idx = (df['#subsystem#'][0][0][0][count]
                        [0][0].flatten()) + time_sum[-1]
            datetime_idx = df['#subsystem#'][0][0][0][count][0][1].flatten()
            step_idx = df['#subsystem#'][0][0][0][count][0][2].flatten()

            # For the cycle number, evaluate if there were missing data.

            if len(cycle_sum) > len(current_sum):
                diff = len(cycle_sum) - len(current_sum)
                cycle_prior = cycle_sum[-1]
                for i in range(0, diff):
                    cycle_sum = np.delete(cycle_sum, -1)
                cycle_idx = (df['#subsystem#'][0][0][0][count]
                             [0][3].flatten()) + cycle_prior
                cycle_test = (df['#subsystem#'][0][0][0]
                              [count][0][3].flatten())
            else:
                cycle_prior = cycle_sum[-1]
                cycle_idx = (df['#subsystem#'][0][0][0][count]
                             [0][3].flatten()) + cycle_prior
                cycle_test = (df['#subsystem#'][0][0][0]
                              [count][0][3].flatten())

            current_idx = df['#subsystem#'][0][0][0][count][0][4].flatten()
            voltage_idx = df['#subsystem#'][0][0][0][count][0][5].flatten()
            charge_ah_idx = df['#subsystem#'][0][0][0][count][0][6].flatten()
            discharge_ah_idx = df['#subsystem#'][0][0][0][count][0][7].flatten(
            )

            # Delete the last curve of the set for each experiment (since it is
            # a single full cycle)
            min_ = np.unique(cycle_idx).min()
            max_ = np.unique(cycle_idx).max()
            idx_for_start = np.argwhere(cycle_idx == min_)[-1]
            idx_for_deletion = np.argwhere(cycle_idx == max_)[0]

            time_idx = time_idx[int(idx_for_start + 1)
                                    :int(idx_for_deletion - 1)]
            datetime_idx = datetime_idx[int(
                idx_for_start + 1):int(idx_for_deletion - 1)]
            step_idx = step_idx[int(idx_for_start + 1)
                                    :int(idx_for_deletion - 1)]
            cycle_idx = cycle_idx[int(idx_for_start + 1)
                                      :int(idx_for_deletion - 1)]
            current_idx = current_idx[int(
                idx_for_start + 1):int(idx_for_deletion - 1)]
            voltage_idx = voltage_idx[int(
                idx_for_start + 1):int(idx_for_deletion - 1)]
            charge_ah_idx = charge_ah_idx[int(
                idx_for_start + 1):int(idx_for_deletion - 1)]
            discharge_ah_idx = discharge_ah_idx[int(
                idx_for_start + 1):int(idx_for_deletion - 1)]

            count = count + 7

            # Concatenate the extracted data
            time_sum = np.concatenate((time_sum, time_idx), axis=0)
            datetime_sum = np.concatenate((datetime_sum, datetime_idx), axis=0)
            step_sum = np.concatenate((step_sum, step_idx), axis=0)
            cycle_sum = np.concatenate((cycle_sum, cycle_idx), axis=0)
            current_sum = np.concatenate((current_sum, current_idx), axis=0)
            voltage_sum = np.concatenate((voltage_sum, voltage_idx), axis=0)
            charge_ah_sum = np.concatenate(
                (charge_ah_sum, charge_ah_idx), axis=0)
            discharge_ah_sum = np.concatenate(
                (discharge_ah_sum, discharge_ah_idx), axis=0)
            if count > (len(df['#subsystem#'][0][0][0]) - 7):
                break

    # Creat a DataFrame from the arrays for each column
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
