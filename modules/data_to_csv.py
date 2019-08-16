import matplotlib.pyplot as plt
import math
from modules.Simpson_BTK import BTK_Diff
import pandas as pd
def Dataplot(parameter,T,df2,my_xaxis,my_yaxis,plot_name):
	
	print("Using btk!")
	V = df2['Vdc'].values
	G= BTK_Diff(parameter,df2[my_xaxis],T)
	G_min = min(min(G),min(df2[my_yaxis]))
	G_max = max(max(G),max(df2[my_yaxis]))
	Internal = (G_max - G_min)/10
	X_Position = max(df2[my_xaxis])/4
	plt.plot(df2[my_xaxis],df2[my_yaxis],label = 'Exp')
	plt.plot(df2[my_xaxis],G,label = 'G/GN Theory')

	plt.text(X_Position, G_min + 4*Internal, 'Temperature:'+str(round(T,4)), fontsize=13)
	plt.text(X_Position, G_min + 3*Internal, 'Delta:'+str(round(parameter[0],4)), fontsize=13)
	plt.text(X_Position, G_min + 2*Internal, 'Gama:'+str(round(parameter[1],4)), fontsize=13)
	plt.text(X_Position, G_min + 1*Internal, 'Barrier Height:'+str(round(parameter[2],4)), fontsize=13)
	plt.text(X_Position, G_min + 0*Internal, 'Spin Polarization:'+str(round(parameter[3],4)), fontsize=13)
	
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
	plt.cla()

