import scipy
import math
from actifs1 import *
import SharpRatio
import OptiActifsFixe

NbActifs = 50
def comparaison():
    res1= scipy.optimize.minimize(SharpRatio.Sharp_Ratio, SharpRatio.x0, method='SLSQP',bounds=None, constraints=SharpRatio.cons,tol=0.01)
    res2= scipy.optimize.minimize(OptiActifsFixe.risque, OptiActifsFixe.x0, method='SLSQP',bounds=None, constraints=OptiActifsFixe.cons,tol=0.01)
  
    
    L1=[]
    L2=[]
    for i in range(len(res1.x)):
            L1.append(round((res1.x[i]*100),2))
            L2.append(round((res2.x[i]*100),2))
    
    sum1=sum([L1[i]*Esp[i] for i in range(len(res1.x))])
    sum2=sum([L2[i]*Esp[i] for i in range(len(res1.x))])
   
        
    print("Sharp Ratio : " ,sum1)
    print("Minimisation du risque : ",sum2)
    
    for i in range(1,5):
        plt.plot([i*d for i in range(len(S[0]))],S[i],label="S"+str(i))
        plt.legend()
    plt.show()
    
comparaison()
    