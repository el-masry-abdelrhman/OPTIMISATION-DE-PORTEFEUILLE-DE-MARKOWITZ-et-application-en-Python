# Créé par CYTech Student, le 25/11/2022 en Python 3.7
import math
import random
import matplotlib.pyplot as plt
import numpy as np
n=1000
T=2
d=T/n
Nmc=100
r=0.1
sigma0=0.5
S0=1
rf=0.001

#cette fonction va permettre de simuler Nmc actifs
def St():
    S=[]
    for i in range(Nmc):
        s=[S0]
        for j in range(1,n):
            s.append(s[j-1]*math.exp((r-(sigma0**2)/2)*d+sigma0*math.sqrt(d)*np.random.randn(1)[0]))
        S.append(s)
    return S
    
Sfixe=[S0]
for i in range(1,n):
    Sfixe.append(Sfixe[i-1]+Sfixe[i-1]*rf)
    
S=[Sfixe]
S=S+St()

def Afficher():
    Temps=[i*d for i in range(n)]
    for i in range(Nmc):
        plt.plot(Temps,S[i])
    plt.show()
    
# on calcule l'espérance
Esp=[sum(s)/len(s) for s in S]

#on calcule la variance
var=[]
for i in range(len(S)):
    somme=0
    for j in range(n):
        somme+= (Esp[i]-S[i][j])**2
    var.append(somme/(n-1))
                   

#on calcule les covariances
cov=[]
for i in range(Nmc+1):
    ligne=[]
    for k in range(Nmc+1):
        c=0
        for j in range(n):
            c+=(S[i][j]-Esp[i])*(S[k][j]-Esp[k])
        ligne.append(c/(n-1))
    cov.append(ligne)
    
Afficher()
    
print(f"Esp = {Esp}" )
print(f"Cov = {cov}")
print(f"Var = {var}")