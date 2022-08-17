from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
from allchaos import Logistic,PWLCM,Singer,Sine,Gaussian,Tent,Bernoulli,Chebyshev,Circle,Cubic,Sinusoidal,ICMIC
from functions_mod import F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell, overlimit
def orders(elem):
    return elem[1]
name=["Logistic","PWLCM","Singer","Sine","Gaussian","Tent","Bernoulli","Chebyshev","Circle","Cubic","Sinusoidal","ICMIC"]
chaos=[Logistic,PWLCM,Singer,Sine,Gaussian,Tent,Bernoulli,Chebyshev,Circle,Cubic,Sinusoidal,ICMIC]
functions=[F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell]
functionname=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17']
domainlist=[100,10,100,100,30,100,1.28,500,5.12,32,600,50,32,30,900,10,5]
maxnumber=100
dimension=30

scores=[0,0,0,0,0,0,0,0,0,0,0,0]
functionorder=0
while(functionorder<17):    
    result=[]
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
        singleresult=[chaosorder,fitnessvalue/maxnumber]
        result.append(singleresult)
        chaosorder+=1
    result.sort(key=orders,reverse=True)
    for var in range(12):
        scores[result[var][0]]+=var
    functionorder+=1

mpl.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置matplotlib整体用Times New Roman
mpl.rcParams['font.weight'] = 'bold'  # 设置matplotlib整体用Times New Roman
mpl.rcParams['font.size'] = 14  # 设置matplotlib整体用Times New Roman
colour=["greenyellow","springgreen","aquamarine","aqua","deepskyblue","blue","blueviolet","violet","deeppink","red","orange","gold"]
hatchs=["/","\\","|","-","--","+","++",".","o","O","*","**"]
bars=plt.bar(name,scores,width=0.8,align="center",hatch='1',color=colour)
for bar,hatch in zip(bars,hatchs):
    bar.set_hatch(hatch)
plt.title("RESULTS RANK",loc="center")
for a,b in zip(name,scores):
    plt.text(a,b,b,ha='center',va="bottom",fontsize=14)
plt.xlabel('map')
plt.ylabel('score')
plt.show()