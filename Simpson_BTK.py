import math
import time
import numpy as np
from scipy.integrate import quad
#Calculate parameters
def calculate_parameters(E,Delta,Gama,Z,T):
    AN = []
    BN = []
    BP = []
    F_E = []
    for number in range(len(E)):
        egama2 = pow(complex(E[number],-Gama),2)
        Delta2 = pow(Delta,2)
        energy_complex = pow((egama2 - Delta2)/egama2,0.5) 
        energy = energy_complex.real
        u02 = (0.5 * (1 + energy))            # coefficient of BCS u0^2
        v02 = (0.5 * (1 - energy))            # coefficient of BCS v0^2
        gama2 = (u02 + Z**2*(u02 - v02))**2
        if abs(complex(E[number],-Gama)) <= Delta:
            AN.append(Delta2/(egama2 + (Delta2 - egama2)*(1+2*Z**2)**2))
            AN[number] = AN[number].real
            BN.append(1 - AN[number])
            BP.append(1)
        else:
            AN.append(u02 * v02/gama2)
            BN.append(pow(u02 - v02,2) * Z*Z * (1 + Z*Z)/gama2)
            BP.append(BN[number])
        F_E.append(math.exp(11.5942*E[number]/T))
    return AN,BN,BP,F_E

# Cut Energy
def split_E(a,n,h):
    E = []                                           # divide the interval
    for i in range(n+1) :
        E.append(a+h*i)
    return E
# Simpson Integration
def integrate_I(V,E,AN,BN,BP,F_E,P,h,T):
    I = []
    time2_start = time.time()
    for m in range(len(V)):
        sum_f_even = 0
        sum_f_odd = 0
        F_V = math.exp(-11.5942*V[m]/T)
        for numberE in range(len(E)):
            # tunneling conductance
            f_e = 1.0/(1+F_E[numberE]*F_V) - 1.0/(1+F_E[numberE])
            f = ((1-P) * (1 + AN[numberE] - BN[numberE]) + P * (1 - BP[numberE]))*f_e
            if numberE == 0:
                f0 = f
            elif numberE == (len(E)-1):
                fn = f
            elif numberE%2 == 0:
                sum_f_even = sum_f_even + f
            else:
                sum_f_odd =  sum_f_odd + f
        I_complex = (h/3)*(f0+fn+2*sum_f_even+4*sum_f_odd)
        I.append(I_complex.real)
    time2_end = time.time()
    print("Integration time:",(time2_end-time2_start),'s')
    return I

# Main Function
def BTK_Diff(parameters,V,T):
    a= -20
    b= 20
    Delta= parameters[0]
    Gama= parameters[1]
    Z= parameters[2]
    P= parameters[3]
    npanel= 1000
    print('Superconducting Gap:' + str(Delta))
    print('Gama:' + str(Gama))
    print('Barrier Height:' + str(Z))
    print('Spin Polarization:' + str(P))
    time_start=time.time()
    #Temperature 
    n = 2 * npanel + 1                               # total number of nodes
    h = (b-a)/n                                      # stepsize
    E = split_E(a,n,h)
    AN,BN,BP,F_E= calculate_parameters(E,Delta,Gama,Z,T)
    I = integrate_I(V,E,AN,BN,BP,F_E,P,h,T)
    dI = []
    dV = []
    G = []
    #if m+1 < len(V):
    #    dV.append(V[m+1] -  V[m])
    for numberV in range(len(V)-1):
        dI.append(I[numberV+1]-I[numberV])
    for numberdI in range(len(dI)):
    	#G.append(round(dI[numberdI]/dV[numberdI],3))
        G.append(dI[numberdI]/dI[numberV]) 
    G.insert(0,1)
    #print(G)
    time_end=time.time()
    print('totally cost:',time_end-time_start,'s')
    return G

