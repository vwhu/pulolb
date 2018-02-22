## Functional Use Cases: 
![Flow Diagram](https://github.com/vwhu/PULOLB/blob/master/Doc/Flow.JPG)
### * Importing and Loading Data: 
#### Components: 
1. Importing data: 
    * **Name**: import_matlab_data
    * **What it does**: Loads the partial discharge data. 
    * **Input**: Dataset in .mat format. 
    * **Output**: Dataset in .mat format. 
2. Loading data: 
    * **Name**: load_matlab_data
    * **What it does**: Imports the data and parses it into a dictionary that resembles a cell array structure. 
    * **Input**: Dataset in .mat format. 
    * **Output**: Dataset in pandas dataframe. 

### * Fitting data into model: 
1. Loading partial discharge data: 
	* **Name**:
	* **What it does**: These can be considered as different 
	classes for the overall data. 
	* **Input**: Partial discharge data. 
	* **Output**: 

2. Fitting a model to the data: 
	* **Name**: Fit_partial_data. 
	* **What it does**: Fits the data using classification?
	* **Input**: Partial discharge data after loading and converting to pandas dataframe.  
	* **Output**: ???

### * 
