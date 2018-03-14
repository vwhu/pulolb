## Data Cleaning Packages

This packages are used to import the charge/discharge cycle infomation inside a Matlab file and load it into two dictionaries sorted by the number of cycle. 

The modules included are:

### 1.  The ``import_data.py`` package

The main function in this package is called ``single_pd_matlab_data``, that generates a dataframe with the data store in a Matlab file using HDF5 format.

### 2.  The ``sort_data.py`` package

This package generates two dictionaries, one for the charge cycles data and the other for the discharge cycles data..


### 3.  The "predict_capacity.py" package

This module is used for predicting the remaining life of lithium batteries. 

There are two main functions in this module. One is called ``partial_to_full``, which links the partial cycle curve to one full cycle curve. The other is called ``get_lifetime``, which gives all the parameters to diagnose the battery using the full cycle curve information. 
This module also includes a set of auxiliar functions that include:

1. ``curve_distance``: Calculates the dynamic time wraping distance between two time series
2. ``distance_cycle_to_full``: Calculates the distances between one partial cycle curve and a set of full cycle curves. 
3. ``life_plot``: This is a visualization function, that plots the results from the prediction method.



