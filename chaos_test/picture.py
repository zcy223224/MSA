from matplotlib import pyplot as plt
import numpy as np
from allchaos import Logistic,PWLCM,Singer,Sine,Gaussian,Tent,Bernoulli,Chebyshev,Circle,Cubic,Sinusoidal,ICMIC
from functions_mod import F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell, overlimit

name=["Logistic","PWLCM","Singer","Sine","Gaussian","Tent","Bernoulli","Chebyshev","Circle","Cubic","Sinusoidal","ICMIC"]
chaos=[Logistic,PWLCM,Singer,Sine,Gaussian,Tent,Bernoulli,Chebyshev,Circle,Cubic,Sinusoidal,ICMIC]
functions=[F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell]
functionname=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17']
domainlist=[100,10,100,100,30,100,1.28,500,5.12,32,600,50,32,30,900,10,5]
result=[]
maxnumber=100
dimension=30


functionorder=16
domain=domainlist[functionorder]
chaosorder=0
while(chaosorder<12):
    fitnessvalue=0
    Individual=[]
    counter=0
    while(counter<maxnumber):
        start=int(np.random.rand()*10000)+500
        Individual=chaos[chaosorder](start,dimension,domain)
        Individual.append(0)
        Individual[dimension]=functions[functionorder](Individual)
        fitnessvalue+=Individual[dimension]
        counter+=1
    result.append(fitnessvalue/maxnumber)
    chaosorder+=1


plt.bar(name,result,width=0.5,align="center",label="mean of fitness",color="red")
plt.title(functionname[functionorder],loc="center")
for a,b in zip(name,result):
    plt.text(a,b,"{:.2e}".format(b),ha='center',va="bottom",fontsize=10)
plt.xlabel('functions')
plt.ylabel('value')
plt.legend()
plt.show()