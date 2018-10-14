import numpy as np
from scipy.optimize import leastsq
from scipy.optimize import fmin_slsqp
from Simpson_BTK import BTK_Diff
import pandas as pd
import time
from btkplot import Dataplot



filename = input("Please input file name: \n")
filename = 'Datas/' + filename
T = input('Please input Temperature : (K) \n')
df2 = pd.read_csv(filename)
# Delta    Gama     Barrier Height    Spin Polarization
bounds = [(0.2,3),(0,2),(0,2),(0,1)]
print("The range of fitting parameters.")
print("Delta : ",bounds[0])
print("Gama  : ",bounds[1])
print("  Z   : ",bounds[2])
print("  P   : ",bounds[3])

# Weightness 
factor = 5

time.sleep(1.5) 

time_start=time.time()
# Rename Columns
def arrange_dataframe(df):
	df.columns = ['Vdc', 'G/GN']
	return df

df2 = arrange_dataframe(df2)

T = float(T)
print("Temperature : ",T)
parameter = [1.0, 0.05, 0.4, 0.3]
V = df2['Vdc'].values
G_experiment = df2['G/GN'].values
G_experiment = list(G_experiment)
print("Data points : ",len(V))
def errors(parameter,V,T,factor):
	G= BTK_Diff(parameter,V,T)
	index_max = G_experiment.index(max(G_experiment))
	index_min = G_experiment.index(min(G_experiment))
	res = 0
	for number in range(len(G)):
		if number < index_max + 15 and number >index_max -15:
			res = res + factor * (G[number] - G_experiment[number])**2
		elif number < index_min + 5 and number >index_min -5:
			res = res + 3*factor * (G[number] - G_experiment[number])**2
		else:
			res = res + (G[number] - G_experiment[number])**2
	return res
''' 梯度下降 '''

r1 = fmin_slsqp(errors,parameter,args=(V,T,factor),iter = 100,bounds = bounds)
#r1 = parameter
print(errors(r1,V,T,factor))
time_end=time.time()
print('Parameters fitting totally cost : ',time_end-time_start)
Dataplot(r1,T,df2,'Vdc','G/GN',filename)
