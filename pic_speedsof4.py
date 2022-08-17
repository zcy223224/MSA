from math import exp, sqrt
from random import randint
import random
from matplotlib import pyplot as plt
import numpy as np
from module.grows import lowbest
from module.chaotic import PWLCM
from module.functions_mod import F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley, Euclid,Perm,Trid,Zakharov,Powell, midstep, overlimit
from module.levy import fly


'''种族个体数'''
maxnumber=100
'''维度'''
dimension=30
'''发现者比例'''
ratep=0.2
ratep2=0.1
'''警戒者比例'''
ratea=0.1
'''安全阈值和危险值'''
ST=0.8
R2=0
'''函数名列表，各函数最大边界和初始边界'''
functions=[F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell]
functionname=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17']
domainlist=[100,10,100,100,30,100,1.28,500,5.12,32,600,50,32,30,900,10,5]

def fitness(elem):
    return elem[dimension]

def OOZ():

    if(randint(0,1)):
        return 1
    else:
        return -1

functionorder=16   
'''最大迭代次数'''
iteration=10
'''最大边界与初始边界'''
domain=domainlist[functionorder]

'''绘图'''
fig = plt.figure()  
ax = fig.add_subplot(1,1,1)
origin_Y=[]
final_Y=[]
wolf_Y=[]
firefly_Y=[]

'''麻雀算法------------------------------------------------------------------------------------------'''
specie=[]
Individual=[]
counter=0
while(counter<maxnumber):
    Individual=list(((np.random.rand(dimension)*2-1)*domain))
    Individual.append(0)
    Individual[dimension]=functions[functionorder](Individual)
    specie.append(Individual)
    counter+=1
specie.sort(key=fitness)

'''算法,开始迭代''' 
n=0
before=[]
while(n<iteration):
    '''发现者更新中'''
    R2=np.random.rand()
    i=0
    while(i<int(maxnumber*ratep)):
        before=[]
        for var in specie[i]:
            before.append(var)
        j=0
        if(R2<ST):
            while(j<dimension):
                '''(iteration*0.5)'''           
                specie[i][j]*=exp((-1)*i/iteration*0.5)
                specie[i][j]=overlimit(domain,specie[i][j])
                j+=1
        else:
            while(j<dimension):           
                specie[i][j]+=np.random.randn()
                specie[i][j]=overlimit(domain,specie[i][j])
                j+=1
        specie[i][dimension]=functions[functionorder](specie[i])
        if(float(before[dimension])<float(specie[i][dimension])):
            specie[i]=before
        i+=1

    specie.sort(key=fitness)

    '''跟随者更新中'''
    while(i<maxnumber):
        before=[]
        for var in specie[i]:
            before.append(var)
        j=0
        if(i>(maxnumber/2)):
            while(j<dimension):
                specie[i][j]=exp((specie[maxnumber-1][j]-specie[i][j])/(i*i))*np.random.randn()
                specie[i][j]=overlimit(domain,specie[i][j])
                j+=1
        else:
            while(j<dimension):
                k=0
                temp0=0
                while(k<dimension):
                    temp0+=OOZ()*(specie[i][k]-specie[0][k])
                    k+=1
                specie[i][j]=specie[0][j]+temp0/dimension
                specie[i][j]=overlimit(domain,specie[i][j])
                j+=1
        specie[i][dimension]=functions[functionorder](specie[i])
        if(float(before[dimension])<float(specie[i][dimension])):
            specie[i]=before
        i+=1

    specie.sort(key=fitness)

    '''警戒者更新中'''
    for i in range(randint(0,5), maxnumber, int(1.0/ratea)):
        before=[]
        for var in specie[i]:
            before.append(var)
        j=0
        if(specie[i][dimension]!=specie[0][dimension]):
            while(j<dimension):
                specie[i][j]=specie[0][j]+(specie[0][j]-specie[i][j])*np.random.randn()
                specie[i][j]=overlimit(domain,specie[i][j])
                j+=1
        else:
            while(j<dimension):
                specie[i][j]+=random.uniform(-1, 1)*(specie[i][j]-specie[maxnumber-1][j])/(specie[i][dimension]-specie[maxnumber-1][dimension]+0.00000001)
                specie[i][j]=overlimit(domain,specie[i][j])
                j+=1
        specie[i][dimension]=functions[functionorder](specie[i])
        if(float(before[dimension])<float(specie[i][dimension])):
            specie[i]=before

    n+=1
    specie.sort(key=fitness)
    origin_Y.append(specie[0][dimension])
'''蠓算法------------------------------------------------------------------------------------------'''
specie=[]
Individual=[]
counter=0
while(counter<maxnumber):
    start=int(np.random.rand()*10000)+500
    Individual=PWLCM(start,dimension,domain)
    Reverse=[]
    for var in Individual:
        if(var>0):
            Reverse.append(domain-var)
        else:
            Reverse.append(-domain-var)
    Reverse.append(0)
    Reverse[dimension]=functions[functionorder](Reverse)
    Individual.append(0)
    Individual[dimension]=functions[functionorder](Individual)
    specie.append(Individual)
    specie.append(Reverse)
    counter+=1
fromlowbest=lowbest(functionorder,dimension)
fromlowbest[dimension]=functions[functionorder](fromlowbest)
specie.append(fromlowbest)
specie.sort(key=fitness)
for var in range(maxnumber+1):
    specie.remove(specie[maxnumber])

n=0
before=[]
while(n<iteration):
    '''发现者更新中'''
    i=0
    while(i<int(maxnumber*ratep2)):
        j=0
        while(j<dimension):
            beforevalueofij=specie[i][j]
            beforevalueoffitness=specie[i][dimension]       
            specie[i][j]+=np.random.randn()*domain*0.3*exp(-n*0.03)
            specie[i][j]=overlimit(domain,specie[i][j])
            specie[i][dimension]=functions[functionorder](specie[i])
            if(beforevalueoffitness<specie[i][dimension]):
                specie[i][j]=beforevalueofij
                specie[i][dimension]=beforevalueoffitness
            j+=1
        i+=1

    specie.sort(key=fitness)

    '''跟随者更新中'''
    while(i<maxnumber):
        j=0
        while(j<dimension):
            specie[i][j]+=midstep(specie[0][j],specie[i][j])
            specie[i][j]=overlimit(domain,specie[i][j])
            j+=1
        specie[i][dimension]=functions[functionorder](specie[i])
        i+=1

    specie.sort(key=fitness)

    '''loser更新中'''
    i=int(maxnumber*(1-ratea))
    while(i<maxnumber):
        before=[]
        for var in specie[i]:
            before.append(var)
        j=0
        while(j<dimension):
            specie[i][j]=0
            j+=1
        for var1 in range(20):
            vectorofLevy=fly(domain,dimension)                                        
            j=0
            while(j<dimension):
                specie[i][j]+=vectorofLevy[j]
                specie[i][j]=overlimit(domain,specie[i][j])
                j+=1
            specie[i][dimension]=functions[functionorder](specie[i])
            if(float(before[dimension])<float(specie[i][dimension])):
                specie[i]=before
            else:
                before=[]
                for var2 in specie[i]:
                    before.append(var2)
        i+=1

    n+=1
    specie.sort(key=fitness)
    final_Y.append(specie[0][dimension])
'''灰狼算法------------------------------------------------------------------------------------------'''
a=2       
specie=[]
Individual=[]
counter=0
while(counter<maxnumber):
    Individual=list(((np.random.rand(dimension)*2-1)*domain))
    Individual.append(0)
    Individual[dimension]=functions[functionorder](Individual)
    specie.append(Individual)
    counter+=1
specie.sort(key=fitness)
n=0
while(n<iteration):
    i=3
    while(i<maxnumber):
        before=[]
        for var in specie[i]:
            before.append(var)
        j=0 
        while(j<dimension):
            da=abs(2*np.random.rand()*specie[0][j])-specie[i][j]
            db=abs(2*np.random.rand()*specie[1][j])-specie[i][j]
            dd=abs(2*np.random.rand()*specie[2][j])-specie[i][j]
            x1=specie[0][j]-(np.random.rand()*2-1)*a*da
            x2=specie[1][j]-(np.random.rand()*2-1)*a*db
            x3=specie[2][j]-(np.random.rand()*2-1)*a*dd          
            specie[i][j]=(x1+x2+x3)/3
            specie[i][j]=overlimit(domain,specie[i][j])
            j+=1
        specie[i][dimension]=functions[functionorder](specie[i])
        if(before[dimension]<specie[i][dimension]):
            specie[i]=before
        i+=1

    n+=1
    a-=2/iteration
    specie.sort(key=fitness)
    wolf_Y.append(specie[0][dimension])
'''萤火虫算法------------------------------------------------------------------------------------------'''
beta0 = 1;   '''最大吸引力'''
gamma = 0.5/domainlist[functionorder];  '''光强吸收系数'''
alpha = 0.2;   '''步长因子'''
specie=[]
Individual=[]
counter=0
while(counter<maxnumber):
    Individual=list(((np.random.rand(dimension)*2-1)*domain))
    Individual.append(0)
    Individual[dimension]=functions[functionorder](Individual)
    specie.append(Individual)
    counter+=1
specie.sort(key=fitness)
n=0
while(n<iteration):
    i=1
    while(i<maxnumber):
        before=[]
        for var in specie[i]:
            before.append(var) 
        j=0 
        while(j<i):
            '''i向所有前方j靠近'''
            r2=Euclid(specie[i],specie[j])
            beta = beta0*exp(-gamma*r2)
            Ii=0
            Ij=0
            k=0
            while(k<dimension):     
                specie[i][k]+=beta*(specie[j][k]-specie[i][k])+alpha*(np.random.rand()-0.5)
                specie[i][k]=overlimit(domain,specie[i][k])                       
                k+=1
            specie[i][dimension]=functions[functionorder](specie[i])
            if(before[dimension]<specie[i][dimension]):
                specie[i]=before
            else:
                before=[]
                for var in specie[i]:
                    before.append(var)                     
            j+=1               
        i+=1
    before=[]
    for var in specie[0]:
        before.append(var)
    k=0
    while(k<dimension):  
        if(n&2==1):   
            specie[0][k]*=exp((-1)*i/(iteration*0.5))
        else:
            specie[0][k]+=np.random.randn()
        k+=1
    specie[0][dimension]=functions[functionorder](specie[0])
    if(before[dimension]<specie[0][dimension]):
        specie[0]=before
    n+=1
    specie.sort(key=fitness)
    firefly_Y.append(specie[0][dimension])
'''------------------------------------------------------------------------------------------'''
ax.plot(origin_Y)
ax.plot(final_Y)
ax.plot(wolf_Y)
ax.plot(firefly_Y)
ax.set_xlabel("iteration")      
ax.set_ylabel("fitness")
fig.suptitle(functionname[functionorder], fontsize = 14, fontweight='bold')
plt.legend(('SSA', 'MSA',"GWO","FA"))
plt.show()