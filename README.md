# Predicting usable lifetime of lithium-ion batteries
PULOLB (/po͝olläb/) is a tool that can determine the remaining lifetime of your battery, based on how you use it. It takes into consideration your usage if you only partially discharge and charge the battery. 
The tool takes in the discharge or charge curve of the current cycle of your battery, whether you partially charge and discharge it and determines the cycle and the capacity of the battery. It finally determines the percentage lifetime of your battery, based on the capacity. 

### SOFTWARE DEPENDENCIES
* Python Version 3.x
* Packages used: dtaidistance, scikit-learn

### PACKAGES INCLUDED IN THE TOOL
* `import_data` is a tool used to take in the input data, and converts the file to be compatible with the tool. 
* `sort_data` sorts the data by the cycle and whether it's charging or discharging data. 
* `predict_capacity` which gives a prediction of the battery's remaining lifetime. 

### FOLDERS IN THE REPOSITORY
* **Pulolb**
Contains the .py files  
	* data - Data used for the training and testing as .mat files. 
	* Test - For unit testing. 
* **Development_in_Notebooks**	
Contains all the software development in jupyter notebooks.
* **Documentation** 
Contains files with information for the use cases, tech reviews and images used in the documentation. 
	* Design.md
	* Tech_Review_222018.pptx
	* DIRECT_PULOLB_Poster.pptx
* **Tutorials**
Contains tutorials and demonstrations to use the tool. 

### SETUP
1. Use `git clone` to copy the repository onto your machine. 
2. Import the packages 

### RUNNING NOSETESTS TO CHECK THE UNITS OF THE CODE
```
MacBook:seds-hw3-Rossana139 martinscavone$ nosetests
...
----------------------------------------------------------------------
Ran 9 tests in 209.989s

OK
```

### ACKNOWLEDGEMENTS
