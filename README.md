# Predicting usable lifetime of lithium-ion batteries
PULOLB (/po͝olläb/) is a tool that can determine the remaining lifetime of your battery, based on how you use it. It takes into consideration your usage if you only partially discharge and charge the battery. 
The tool takes in the discharge or charge curve of the current cycle of your battery, whether you partially charge and discharge it and determines the cycle and the capacity of the battery. It finally determines the percentage lifetime of your battery, based on the capacity. 

### SOFTWARE DEPENDENCIES
* Python Version 3.6
* Packages used: fastdtw, h5py, hdf5storage, matplotlib, numpy, pandas, scipy, tqdm

### PACKAGES INCLUDED IN THE TOOL
* `import_data` is a tool used to take in the input data, and converts the file to be compatible with the tool. 
* `sort_data` sorts the data by the cycle and whether it's charging or discharging data. 
* `predict_capacity` which gives a prediction of the battery's remaining lifetime. 

### FOLDERS IN THE REPOSITORY
* **pulolb**
Contains the .py files  
	* data - Data used for the training and testing as .mat files. 
	* Test - For unit testing. 
* **development_in_notebooks**	
Contains all the software development in jupyter notebooks.
* **documentation** 
Contains files with information for the use cases, tech reviews and images used in the documentation. 
	* Design.md
	* Tech_Review_222018.pptx
	* DIRECT_PULOLB_Poster.pptx
	* DIRECT_PULOLB_Poster.pdf
* **tutorials**
Contains tutorials and demonstrations to use the tool. 

### SETUP
1. Use `git clone` to copy the repository onto your machine. 
2. Import the packages 

### RUNNING NOSETESTS TO CHECK THE UNITS OF THE CODE
```
MacBook: martinscavone$ nosetests
...
----------------------------------------------------------------------
Ran 9 tests in 209.989s

OK
```

### ACKNOWLEDGEMENTS

We would like to thank Professor David Beck and the group of teaching assistants in the DIRECT program for all the help and guidance regarding the development of this software.

We would also like to thank the Center for Advanced Life Cycle Engineering (CALCE) from the University of Maryland for providing the data in an open-source platform, the University of Washington for their continued support, and the Clean Energy Institute for making the DIRECT program possible.

