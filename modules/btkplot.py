import matplotlib.pyplot as plt
import math
from Simpson_BTK import BTK_Diff
import pandas as pd
def Dataplot(parameter,T,df2,my_xaxis,my_yaxis,plot_name):
	
	print("Using btk!")
	V = df2['Vdc'].values
	G= BTK_Diff(parameter,df2[my_xaxis],T)
	# 原点相交
	'''
	fig = plt.gca()
	fig.xaxis.set_ticks_position('bottom')
	fig.spines['bottom'].set_position(('data',0))
	fig.yaxis.set_ticks_position('left')
	fig.spines['left'].set_position(('data',0))
	'''
	# 去掉边框
	'''
	fig.spines['top'].set_color('none')
	fig.spines['right'].set_color('none')
	'''
	# Axis Setting	
	#plt.figure(figsize=(7,4)) #画布大小
	plt.plot(df2[my_xaxis],df2[my_yaxis],label = 'Exp')
	plt.plot(df2[my_xaxis],G,label = 'G/GN Theory')

	plt.text(2.2, 0.95, 'Temperature:'+str(round(T,4)), fontsize=10)
	plt.text(2.2, 0.9, 'Delta:'+str(round(parameter[0],4)), fontsize=10)
	plt.text(2.2, 0.85, 'Gama:'+str(round(parameter[1],4)), fontsize=10)
	plt.text(2.2, 0.8, 'Barrier Height:'+str(round(parameter[2],4)), fontsize=10)
	plt.text(2.2, 0.75, 'Spin Polarization:'+str(round(parameter[3],4)), fontsize=10)
	#plt.scatter(df.x, df.y)
	#plt.plot(df.y,'b',lw = 1.5) # 蓝色的线
	#plt.plot(y.cumsum(),'ro') #离散的点
	#plt.grid(True)
	'''      图例位置设置
	     plt.legend(loc='lower left')
	 0: ‘best'         1: ‘upper right' 
	 2: ‘upper left'   3: ‘lower left' 
	 4: ‘lower right'  5: ‘right' 
	 6: ‘center left'  7: ‘center right' 
	 8: ‘lower center' 9: ‘upper center' 
	 10: ‘center'
	'''
	plt.legend(loc = 1)
	plt.axis('tight')
	plt.xlabel(my_xaxis)
	plt.ylabel(my_yaxis)
	#Change Name
	plot_name = plot_name[:-4]

	plt.title(plot_name)
	# Savefig
	plt.savefig(plot_name + '.png')
	# Save Data
	data = {'V': V, 'G/GN': G}
	data_df = pd.DataFrame(data)
	data_df.to_csv(plot_name +'_BTK_Fit.csv')

	plt.show()
