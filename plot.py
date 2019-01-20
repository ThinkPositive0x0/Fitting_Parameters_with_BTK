import numpy as np
from scipy.optimize import leastsq
from Simpson_BTK import BTK_Diff
import pandas as pd
import time
from btkplot import Dataplot
time_start=time.time()
filename1 = 'b2.csv'
df2 = pd.read_csv('b2.csv')

# Rename Columns
def arrange_dataframe(df):
	df.columns = ['Vdc', 'G/GN']
	return df

df2 = arrange_dataframe(df2)

T = input('Please input Temperature :    (K) \n')
T = float(T)
print("Temperature : ",T)
parameter = [0.731,0.08,0.36,0.36]
time_end=time.time()
print('Parameters fitting totally cost : ',time_end-time_start)
Dataplot(parameter,T,df2,'Vdc','G/GN',filename1)

