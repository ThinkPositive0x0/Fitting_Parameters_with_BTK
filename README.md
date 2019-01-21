# Fitting_Parameters_with_BTK
## Contributors: ThinkPositive0x0  Tripodcat  Date: 2019.1.21  Version: 2.0
## How to use it.
The variable 'bounds' means the boundary of delta, gama, barrier height and spin polarization.

Input file type must be .csv. 

	Example: example.csv

The list parameter: parameter = [Delta, Gama, Z, P] 


Variable 'factor' is the weightness of peaks and valleys. P.S. 5 for 1000 experiment data points may be a good setting.

## C Vesion Updates
If it cannot be used with the c library, compile the shared library again.

Compile library code:
	
	gcc -Wall -shared -O3 -lm -o libSimpson_BTK.so Simpson_BTK.c

If previous code not working, please try:
	
	gcc -Wall -shared -fPIC -O3 -lm -std=c99 -o libSimpson_BTK.so Simpson_BTK.c
	
Please note that working on a Linux system should make some changes to the file module/Simpson_BTK.py and recompile Simpson_BTK.c.

	dllpath = curPath + "\\modules   
	dllfile = curPath + "\\modules\\libSimpson_BTK.so"
	
	change into 
	
	dllpath = curPath + "/modules   
	dllfile = curPath + "/modules/libSimpson_BTK.so"
