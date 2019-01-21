import numpy as np
from scipy.optimize import fmin_slsqp
from modules.Simpson_BTK import BTK_Diff
import pandas as pd
import time
from modules.data_to_csv import Dataplot
import random

# Rename Columns
def arrange_dataframe(df):
	df.columns = ['Vdc', 'G/GN']
	return df

def errors(parameter,V,T,factor,G_experiment):
	G= BTK_Diff(parameter,V,T)
	index_max = G_experiment.index(max(G_experiment))
	index_max_2 = len(V) - index_max
	index_min = G_experiment.index(min(G_experiment))
	res = 0
	for number in range(len(G)):
		if number < index_max + 25 and number >index_max -25:
			res = res + factor * (G[number] - G_experiment[number])**2
		elif number < index_max_2 + 25 and number >index_max_2 -25:
			res = res + factor * (G[number] - G_experiment[number])**2
		elif number < index_min + 11 and number >index_min -11:
			res = res + 6 * factor * (G[number] - G_experiment[number])**2
		else:
			res = res + (G[number] - G_experiment[number])**2
	return res

def run_parameter(filenames,Ts,bound):
	for number in range(len(filenames)):
		filename = 'Datas/' + filenames[number]
		df2 = pd.read_csv(filename)
		# Delta    Gama     Barrier Height    Spin Polarization
		bounds = bound[number]
		print("The range of fitting parameters.")
		print("Delta : ",bounds[0])
		print("Gama  : ",bounds[1])
		print("  Z   : ",bounds[2])
		print("  P   : ",bounds[3])

		time.sleep(0.5) 

		time_start=time.time()


		df2 = arrange_dataframe(df2)

		T = float(Ts[number])

		print("Temperature : ",T)
		parameter = [1.3, 0.4, 1.5, 0.0]
#		for i in range(4):
#			parameter[i] += random.uniform(0,0.1)
		print('Parameters: ',parameter)
		V = df2['Vdc'].values
		G_experiment = df2['G/GN'].values
		G_experiment = list(G_experiment)
		print("Data points : ",len(V))

		''' 梯度下降 '''
		# Weightness 
		factor = 38
		# annealing
		myerror = []
		myparameter = []

		for i in range(13):
			
			r1 = fmin_slsqp(errors,parameter,args=(V,T,factor,G_experiment),iter = 100,bounds = bounds)
			#r1 = parameter
			print('\n**************************')
			print('\nSuperconducting Gap:' + str(round(r1[0],4)))
			print('Gama:' + str(round(r1[1],4)))
			print('Barrier Height:' + str(round(r1[2],4)))
			print('Spin Polarization:' + str(round(r1[3],4)))
			myerror.append(errors(r1,V,T,factor,G_experiment))
			myparameter.append(r1)
			for j in range(4):
				parameter[j] = r1[j] + random.uniform(-0.1,0.1)
				#parameter[j] = r1[j] + random.uniform(-0.013*(9-i),0.013*(9-i))
				if parameter[j] < 0:
					parameter[j] = 0
			print('errors: ',myerror[i])

		min_error_index = myerror.index(min(myerror))
		r1 = fmin_slsqp(errors,myparameter[min_error_index],args=(V,T,factor,G_experiment),iter = 100,bounds = bounds)
		print('errors: ',errors(r1,V,T,factor,G_experiment))
		time_end=time.time()
		print('**************************')
		print('Parameters fitting totally cost : ',round(time_end-time_start,4),'s !')
		print('**************************')
		Dataplot(r1,T,df2,'Vdc','G/GN',filename)

if __name__ == "__main__":
	filenames = ['b2.csv','t1.csv']
	Ts = [1.6,1.66]
	bound = [[(0.5,2),(0,2),(0,10),(0,1)],[(0.5,2),(0,2),(0,10),(0,1)]]
	run_parameter(filenames,Ts,bound)
