# Fitting_Parameters_with_BTK
## Contributors: ThinkPositive0x0  Date: 2018.10.14  Version: 1.0
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

