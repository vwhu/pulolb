## Unit tests for Cleaning Data packages

This unit tests are for the modules``import_data``, ``sort_data``, and ``predict_capacity``. 
Including here are the tests for every function in each module:

### Functions tested in ``import_data`` module:

1. ``import_matlab_data`` 
2. ``initialize_datasets`` 
3. ``single_pd_matlab_data``

### Functions tested in ``sort_data`` module:

1. ``by_cycle`` 
2. ``charge_discharge``

### Functions tested in ``predict_capacity`` module:

1. ``curve_distance``
2. ``distance_cycle_to_full``
3. ``partial_to_full``
4. ``get_lifetime``

### Nosetests result:

Ran 9 tests in 209.989s

OK