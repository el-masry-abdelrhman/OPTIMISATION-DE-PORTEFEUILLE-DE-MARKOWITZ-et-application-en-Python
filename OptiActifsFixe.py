import scipy
import math
from actifs1 import *

R0=0.1
NbActifs = 50

x0=[0 for i in range(NbActifs)]
cons=({'type':'eq','fun': lambda x: sum(x)-1},
          {'type':'ineq','fun': lambda x: sum([x[i]*Esp[i] for i in range(1,NbActifs)])+(x[0]*rf)-R0},
          {'type':'ineq','fun': lambda x: x})

#on minimise le risque lié au portefeuille d'actifs (S0,...,Sn)

def risque(x):
    s=0
    for i in range(len(x)):
        for j in range(len(x)):
            s+=x[i]*x[j]*cov[i][j]
    return s

def OptiRisque_ActifFixe():
#on défini les contraintes : sum(x)=1 et Xi>=0 pour tout i
    x0=[0 for i in range(NbActifs)]
    cons=({'type':'eq','fun': lambda x: sum(x)-1},
          {'type':'ineq','fun': lambda x: sum([x[i]*Esp[i] for i in range(1,NbActifs)])+(x[0]*rf)-R0},
          {'type':'ineq','fun': lambda x: x})
#on minimise la fonction risque en tenant compte des contraintes
    res = scipy.optimize.minimize(risque, x0, method='SLSQP',bounds=None, constraints=cons)

#si on trouve un résultat alors on renvoie celui-ci
    L=[]
    if res.success==True:
        for i in range(len(res.x)):
            L.append(round((res.x[i]*100),2))
            print('X'+str(i)+" = "+str(L[i]))
        print(sum([L[i]*Esp[i] for i in range(NbActifs)]))
    else:
        print("Il n'y a pas de solution")
    return L

OptiRisque_ActifFixe()

