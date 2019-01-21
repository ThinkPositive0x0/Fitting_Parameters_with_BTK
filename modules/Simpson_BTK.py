import math
import time
import numpy as np
from scipy.integrate import quad
import ctypes
import os


# Main Function
def BTK_Diff(parameters,V,T):
    Delta, Gama, Z, P = parameters
    a= -20
    b= 20
    npanel= 1000
    #print('Superconducting Gap:' + str(Delta))
    #print('Gama:' + str(Gama))
    #print('Barrier Height:' + str(Z))
    #print('Spin Polarization:' + str(P))
    #time_start=time.time()
    #Temperature 
    n = 2 * npanel + 1                          # total number of nodes
    h = (b-a)/n                                 # stepsize
    E = [a + h*i for i in range(n+1)]           # split E

    VN = len(V)
    EN = len(E)
    Vp = (ctypes.c_double * VN)(*V)             # Convert V into C array Vp
    Ep = (ctypes.c_double * EN)(*E)             # Convert E into C array Ep
    Gp = (ctypes.c_double * VN)()               # Array Gp to store the answer
    Tp = ctypes.c_double(T)
    Deltap = ctypes.c_double(Delta)
    Gamap = ctypes.c_double(Gama)
    Zp = ctypes.c_double(Z)
    Pp = ctypes.c_double(P)
    hp = ctypes.c_double(h)

    # Call wrapper to calculate
    curPath = os.getcwd()
    dllpath = curPath + "\\modules"
    dllfile = curPath + "\\modules\\libSimpson_BTK.so"
    os.chdir(dllpath)
    wrapper = ctypes.CDLL(dllfile)
    os.chdir(curPath)
    wrapper.c_BTK_Diff(Ep, EN, Vp, VN, Tp, Deltap, Gamap, Zp, Pp, hp, Gp)
    G = [*Gp]

    #print(G)
    #time_end=time.time()
    #print('totally cost:',time_end-time_start,'s')
    return G