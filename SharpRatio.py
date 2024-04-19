import scipy
import math
from actifs1 import *

NbActifs = 50
x0=[0.5 for i in range(NbActifs)]
cons=[{'type':'eq','fun': lambda x: sum(x)-1},# contraintes pour avoir la sommes des Xi = 1
          {'type':'ineq','fun': lambda x: x}]

#on minimise le risque lié au portefeuille d'actifs (S0,...,Sn)
def Gains(x):
    return sum([x[i]*Esp[i] for i in range(1,len(x))])-rf

def risque(x):
    s=0
    for i in range(1,NbActifs):
        for j in range(1,NbActifs):
            s+=x[i]*x[j]*cov[i][j]
    return s

def Sharp_Ratio(x):
    return -Gains(x)/math.sqrt(risque(x))

#on défini les contraintes : sum(x)=1 et Xi>=0 pour tout i
def OptiSharpRatio():
    x0=[0.5 for i in range(NbActifs)]
    cons=[{'type':'eq','fun': lambda x: sum(x)-1},# contraintes pour avoir la sommes des Xi = 1
          {'type':'ineq','fun': lambda x: x}] #contraintes pour rendre les Xi positifs

#on minimise la fonction risque en tenant compte des contraintes
    res = scipy.optimize.minimize(Sharp_Ratio, x0, method='SLSQP',bounds=None, constraints=cons,tol=0.01)

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

OptiSharpRatio()