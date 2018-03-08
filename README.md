# PREDICTING THE LIFETIME OF YOUR BATTERY
PULOLB (/po͝olläb/) is a tool that can determine the remaining lifetime of your battery, based on how you use it. It takes into consideration your usage if you only partially discharge and charge the battery. 
The tool takes in the discharge or charge curve of the current cycle of your battery, whether you partially charge and discharge it and determines the cycle and the capacity of the battery. It finally determines the percentage lifetime of your battery, based on the capacity. 

### SOFTWARE DEPENDENCIES
* Python Version 3.x
* Packages used: dtaidistance, scikit-learn

### PACKAGES INCLUDED IN THE TOOL
* `import_data` is a tool used to take in the input data, and converts the file to be compatible with the tool. 
* `sort_data` sorts the data by the cycle and whether it's charging or discharging data. 
* `ML` Machine learning package goes here. 

### FOLDERS IN THE REPOSITORY
* **PULOLB**
Contains the .py files 
	* Development_in_Notebooks - All the .ipynb files used to develop the tool. 
	* data - Data used for the training and testing as .mat files. 
	* Test - For unit testing. 
* **DOC** 
Contains files with information for the use cases, tech reviews and images used in the documentation. 
	* Design.md
	* Tech_Review_222018.pptx
	*
* **EXAMPLES**
Contains demonstrations to use the tool. 
	*
	*

### SETUP
1. Use `git clone` the repository onto your machine. 
2. 
3. 

### RUNNING NOSETESTS TO CHECK THE UNITS OF THE CODE

### ACKNOWLEDGEMENTS
