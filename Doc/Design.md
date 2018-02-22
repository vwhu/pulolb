## Functional Use Cases: 
![Flow Diagram](https://github.com/vwhu/PULOLB/blob/master/Doc/images/Flow.JPG)
### * Importing and Loading Data: 
#### Components: 
1. Importing data: 
    * **Name**: import_matlab_data
    * **What it does**: Loads the training discharge data. 
    * **Input**: Dataset in .mat format. 
    * **Output**: Dataset in .mat format. 
2. Loading data: 
    * **Name**: load_matlab_data
    * **What it does**: Imports the data and parses it into a dictionary that resembles a cell array structure. 
    * **Input**: Dataset in .mat format from `import_matlab_data`. 
    * **Output**: Dataset in pandas dataframe. 

### * Model training: 
#### Components: 
1. Fitting a model to the data: 
	* **Name**: train_model
	* **What it does**: Imports and loads the data using `import_matlab_data` and `load_matlab_data`. Trains the classification model. 
	* **Input**: Training discharge data after loading and converting to pandas dataframe with `load_matlab_data`.
	* **Output**: ???

### * Classification and Prediction:
#### Components: 
1. Classification of the test data:
	* **Name**: classify_data
    * **What it does**: Imports and loads the data using `import_matlab_data` and `load_matlab_data`. Classifies the test data to the best fit of the full discharge curve to predict the full discharge curve. 
    * **Input**: Test dataset after conversion to pandas dataframe with `import_matlab_data`. 
    * **Output**: Full discharge curve data in pandas dataframe. 
2. Prediction of battery life:
	* **Name**: predict_battery_life:
    * **What it does**: Determines the capacity from the full discarge curve from `classify_data` and calculates the percentage of life remaining in the battery. 
    * **Input**: Full discharge curve data from `classify_data` as pandas dataframe. 
    * **Output**: Percentage as float.  

### * Visualization:
#### Components: 
1. Remaining usable life (RUL):
	* **Name**: plot_battery_life
	* **What it does**: Imports the percentage from `predict_battery_life` 
	and does a linear extrapolation to predict when the battery will die. 
	* **Input**: Percentage as float from `predict_battery_life` and time elasped since the battery has been used as a float. 
	* **Output**: A matplotlib.pyplot plot of time and battery life. 
	