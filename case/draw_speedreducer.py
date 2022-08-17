from math import exp, gamma, sin, sqrt
from random import randint
import random
import numpy as np
from matplotlib import pyplot as plt

def midstep(a,b):
    if((a-b)**3==0):        
        return (a-b)*0.1
    c=(np.random.rand()+1)/(a-b)**3
    if(c<-50):
        c=-50
    if(c>50):
        c=50
    g=1/(1+exp(-c))
    s=(a-b)*(0.1+g/10)
    return s

def Euclid(posA:list,posB:list):
    lena=len(posA)-1
    temp0=0
    i=0
    while(i<lena):
        temp0+=(posA[i]-posB[i])*(posA[i]-posB[i])
        i+=1
    temp0=float(temp0)
    temp0=sqrt(temp0)
    return temp0
'''种族个体数'''
maxnumber=100
'''维度'''
dimension=7
'''最大边界与初始边界'''
ldomain=[2.6,0.7,17,7.3,7.8,2.9,5.0]
hdomain=[3.6,0.8,28,8.3,8.3,3.9,5.5]
pi=3.141592654

testnum=1
def OOZ():
    if(randint(0,1)):
        return 1
    else:
        return -1
        
def fly(dimension):
    beta=1.5
    u = (gamma(1+beta)*sin(pi*beta/2)/(gamma((1+beta)/2)*beta*2**((beta-1)/2)))**(1/beta)
    u = np.random.randn()*u
    v = np.random.randn()
    s = u/(abs(v))**(1/beta)
    steplength=abs(s)
    RatioDimension=np.random.rand(dimension)*2-1
    Ratiolength=0
    for levyvar in RatioDimension:
        Ratiolength+=levyvar**2
    Ratiolength=sqrt(Ratiolength)
    levyi=0
    while(levyi<dimension):
        RatioDimension[levyi]*=0.5*(hdomain[levyi]-ldomain[levyi])*steplength/Ratiolength
        levyi+=1
    return RatioDimension

def PWLCM(start):
    st=[]
    temp=0.2*(np.random.rand()+0.001)
    p=0.62
    i=0
    st.append(temp)
    while(i<start):
        if(st[i]<p):
            temp=st[i]/p
        else:
            temp=(1-st[i])*(1-p)
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        if(z[i-start]<p):
            temp=z[i-start]/p
        else:
            temp=(1-z[i-start])*(1-p)
        i+=1
        z.append(temp)
    for var in range(dimension):
        i=np.random.rand()-0.5
        if(i>=0):
            z[var]=z[var]*(hdomain[var]-ldomain[var])/2+(hdomain[var]+ldomain[var])/2
        else:
            z[var]=-1*z[var]*(hdomain[var]-ldomain[var])/2+(hdomain[var]+ldomain[var])/2
    return z

def fitness(elem):
    return elem[dimension]

def overlimit(x):
    b=x[0]
    m=x[1]
    z=x[2]
    l1=x[3]
    l2=x[4]
    d1=x[5]
    d2=x[6]
    bool=1
    if(b<ldomain[0] or b>hdomain[0] or m<ldomain[1] or m>hdomain[1] or z<ldomain[2] or z>hdomain[2] or l1<ldomain[3] or l1>hdomain[3]):
        bool=0
    if(l2<ldomain[4] or l2>hdomain[4] or d1<ldomain[5] or d1>hdomain[5] or d2<ldomain[6] or d2>hdomain[6]):
        bool=0
    return bool

def lowbest():
    num=20   
    result=[]
    for var in range(dimension):
        result.append((hdomain[var]+ldomain[var])/2)
    result.append(0)
    dorder=0
    result[dimension]=fitnessfunction(result)
    while(dorder<dimension):
        down=ldomain[dorder]
        step=(hdomain[dorder]-ldomain[dorder])/num
        best=(hdomain[dorder]+ldomain[dorder])/2
        for time in range(5):       
            for i in range(num-1):
                tempd=result[dorder]
                result[dorder]=down+step*(i+1)
                tempr=fitnessfunction(result)
                if(result[dimension]>tempr):
                    best=down+step*(i+1)
                    result[dimension]=tempr
                else:
                    result[dorder]=tempd
            down=best-step          
            step=2*step/num
        result[dorder]=best
        dorder+=1
    if(overlimit(result)==0):
        result=[]
        for var in range(dimension):
            result.append((hdomain[var]+ldomain[var])/2)
        result.append(0)
        result[dimension]=fitnessfunction(result)
    return result

def fitnessfunction(x):    
    result2=0
    b=x[0]
    m=x[1]
    z=x[2]
    l1=x[3]
    l2=x[4]
    d1=x[5]
    d2=x[6]
    M=745*l1/(m*z)
    H=745*l2/(m*z)
    temp1=(0.7854*b*m**2)*(3.3333*z**2+14.9334*z-43.0934)
    temp2=1.508*b*(d1**2+d2**2)
    temp3=7.4777*(d1**3+d2**3)
    temp4=0.7854*(l1*d1**2+l2*d2**2)
    result1=temp1-temp2+temp3+temp4
    g=[]
    g.append(27/(b*m**2*z)-1)
    g.append(397.5/(b*m**2*z**2)-1)
    g.append(1.93*l1**3/(m*z*d1**4)-1)
    g.append(1.93*l2**3/(m*z*d2**4)-1)
    g.append(sqrt(M**2+16900000)/(110*d1**3)-1)
    g.append(sqrt(H**2+157500000)/(85*d2**3)-1)
    g.append(m*z/40-1)
    g.append(5*m/b-1)
    g.append(b/(12*m)-1)
    tempg=0
    for var in g:
        if(var>0):
            tempg+=var*10000
    result2=result1+tempg
    if(testnum==0):
        print(g)
    return result2


'''绘图'''
fig = plt.figure()  
ax = fig.add_subplot(1,1,1)
origin_Y=[]
final_Y=[]
wolf_Y=[]
firefly_Y=[]
'''MSA---------------------------------------------------------------------------------------------------'''
def MSA():
    ratep=0.3
    ratea=0.3
    specie=[]
    Individual=[]
    counter=0
    while(counter<maxnumber):
        start=int(np.random.rand()*10000)+500
        Individual=PWLCM(start)
        Reverse=[]
        for var in range(dimension):
            Reverse.append(hdomain[var]+ldomain[var]-Individual[var])
        Reverse.append(0)
        Reverse[dimension]=fitnessfunction(Reverse)
        Individual.append(0)
        Individual[dimension]=fitnessfunction(Individual)
        specie.append(Individual)
        specie.append(Reverse)
        counter+=1

    fromlowbest=lowbest()
    fromlowbest[dimension]=fitnessfunction(fromlowbest)
    specie.append(fromlowbest)
    specie.sort(key=fitness)
    for var in range(maxnumber+1):
        specie.remove(specie[maxnumber])
    
    '''算法,开始迭代''' 
    '''最大迭代次数'''
    iteration=500
    n=0
    before=[]
    while(n<iteration):
        i=0
        while(i<int(maxnumber*ratep)):
            j=0
            while(j<dimension):
                beforevalueofij=specie[i][j]
                beforevalueoffitness=specie[i][dimension]       
                specie[i][j]+=np.random.randn()*(hdomain[j]-ldomain[j])*0.3*exp(-n*0.03)
                specie[i][dimension]=fitnessfunction(specie[i])
                if(beforevalueoffitness<specie[i][dimension] or overlimit(specie[i])==0):
                    specie[i][j]=beforevalueofij
                    specie[i][dimension]=beforevalueoffitness
                j+=1
            i+=1

        specie.sort(key=fitness)

        while(i<maxnumber):
            j=0
            while(j<dimension):
                beforevalueofij=specie[i][j]
                specie[i][j]+=midstep(specie[0][j],specie[i][j])
                if(overlimit(specie[i])==0):
                    specie[i][j]=beforevalueofij
                j+=1
            specie[i][dimension]=fitnessfunction(specie[i])
            i+=1

        specie.sort(key=fitness)

        i=int(maxnumber*(1-ratea))
        while(i<maxnumber):
            before=[]
            for var in specie[i]:
                before.append(var)
            j=0
            while(j<dimension):
                specie[i][j]=(hdomain[j]+ldomain[j])/2
                j+=1
            for var1 in range(20):
                vectorofLevy=fly(dimension)                                        
                j=0
                while(j<dimension):
                    beforevalueofij=specie[i][j]
                    specie[i][j]+=vectorofLevy[j]
                    if(overlimit(specie[i])==0):
                        specie[i][j]=beforevalueofij
                    j+=1
                specie[i][dimension]=fitnessfunction(specie[i])
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
'''SSA---------------------------------------------------------------------------------------------------'''
def SSA():
    ratep=0.2
    ratea=0.1
    ST=0.8
    R2=0
    specie=[]
    Individual=[]
    counter=0
    while(counter<maxnumber):
        Individual=PWLCM(int(np.random.rand()*10000)+500)
        Individual.append(0)
        Individual[dimension]=fitnessfunction(Individual)
        specie.append(Individual)
        counter+=1
    specie.sort(key=fitness)
    
    '''算法,开始迭代''' 
    '''最大迭代次数'''
    iteration=500
    n=0
    before=[]
    while(n<iteration):
        '''发现者更新中'''
        i=0
        while(i<int(maxnumber*ratep)):
            before=[]
            for var in specie[i]:
                before.append(var)
            j=0
            R2=np.random.rand()
            if(R2<ST):
                while(j<dimension):
                    beforevalueofij=specie[i][j]           
                    specie[i][j]*=exp((-1)*i/(iteration*0.5))
                    if(overlimit(specie[i])==0):
                        specie[i][j]=beforevalueofij
                    j+=1
            else:
                while(j<dimension):
                    beforevalueofij=specie[i][j]           
                    specie[i][j]+=np.random.randn()
                    if(overlimit(specie[i])==0):
                        specie[i][j]=beforevalueofij
                    j+=1
            specie[i][dimension]=fitnessfunction(specie[i])
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
                    beforevalueofij=specie[i][j]
                    specie[i][j]=exp((specie[maxnumber-1][j]-specie[i][j])/(i*i))*np.random.randn()
                    if(overlimit(specie[i])==0):
                        specie[i][j]=beforevalueofij
                    j+=1
            else:
                while(j<dimension):
                    k=0
                    temp0=0
                    while(k<dimension):
                        temp0+=OOZ()*(specie[i][k]-specie[0][k])
                        k+=1
                    beforevalueofij=specie[i][j]
                    specie[i][j]=specie[0][j]+temp0/dimension
                    if(overlimit(specie[i])==0):
                        specie[i][j]=beforevalueofij
                    j+=1
            specie[i][dimension]=fitnessfunction(specie[i])
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
                    beforevalueofij=specie[i][j]
                    specie[i][j]=specie[0][j]+(specie[0][j]-specie[i][j])*np.random.randn()
                    if(overlimit(specie[i])==0):
                        specie[i][j]=beforevalueofij
                    j+=1
            else:
                while(j<dimension):
                    beforevalueofij=specie[i][j]
                    specie[i][j]+=0
                    specie[i][j]+=random.uniform(-1, 1)*(specie[i][j]-specie[maxnumber-1][j])/(specie[i][dimension]-specie[maxnumber-1][dimension]+0.00000001)
                    if(overlimit(specie[i])==0):
                        specie[i][j]=beforevalueofij
                    j+=1
            specie[i][dimension]=fitnessfunction(specie[i])
            if(float(before[dimension])<float(specie[i][dimension])):
                specie[i]=before

        n+=1
        specie.sort(key=fitness)
        origin_Y.append(specie[0][dimension])    
'''GWO---------------------------------------------------------------------------------------------------'''
def GWO():
    a=2
    specie=[]
    Individual=[]
    counter=0
    while(counter<maxnumber):
        Individual=PWLCM(int(np.random.rand()*10000)+500)
        Individual.append(0)
        Individual[dimension]=fitnessfunction(Individual)
        specie.append(Individual)
        counter+=1
    specie.sort(key=fitness)
    
    '''算法,开始迭代''' 
    '''最大迭代次数'''
    iteration=500
    n=0
    before=[]
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
                beforevalueofij=specie[i][j]          
                specie[i][j]=(x1+x2+x3)/3
                if(overlimit(specie[i])==0):
                        specie[i][j]=beforevalueofij
                j+=1
            specie[i][dimension]=fitnessfunction(specie[i])
            if(before[dimension]<specie[i][dimension]):
                specie[i]=before
            i+=1

        n+=1
        a-=2/(iteration)
        specie.sort(key=fitness)
        wolf_Y.append(specie[0][dimension])
'''FA---------------------------------------------------------------------------------------------------'''
def FA():
    beta0 = 1;   '''最大吸引力'''
    alpha = 0.2;   '''步长因子'''
    specie=[]
    Individual=[]
    counter=0
    while(counter<maxnumber):
        Individual=PWLCM(int(np.random.rand()*10000)+500)
        Individual.append(0)
        Individual[dimension]=fitnessfunction(Individual)
        specie.append(Individual)
        counter+=1
    specie.sort(key=fitness)
    
    '''算法,开始迭代''' 
    '''最大迭代次数'''
    iteration=500
    n=0
    before=[]
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
                k=0
                while(k<dimension):                        
                    gamma = 1/(hdomain[k]-ldomain[k]);  '''光强吸收系数'''
                    beta = beta0*exp(-gamma*r2)
                    beforevalueofij=specie[i][k]     
                    specie[i][k]+=beta*(specie[j][k]-specie[i][k])+alpha*(np.random.rand()-0.5)
                    if(overlimit(specie[i])==0):
                        specie[i][k]=beforevalueofij                       
                    k+=1
                specie[i][dimension]=fitnessfunction(specie[i])
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
            beforevalueofij=specie[0][k]  
            if(n&2==1):   
                specie[0][k]*=exp((-1)*i/(iteration*0.5))
            else:
                specie[0][k]+=np.random.randn()
            k+=1
            if(overlimit(specie[0])==0):
                specie[0][k]=beforevalueofij
        specie[0][dimension]=fitnessfunction(specie[0])
        if(before[dimension]<specie[0][dimension]):
            specie[0]=before
        n+=1
        specie.sort(key=fitness)
        firefly_Y.append(specie[0][dimension])
'''---------------------------------------------------------------------------------------------------'''
SSA()
MSA()
GWO()
FA()
ax.plot(origin_Y)
ax.plot(final_Y)
ax.plot(wolf_Y)
ax.plot(firefly_Y)
ax.set_xlabel("iteration")      
ax.set_ylabel("fitness")
fig.suptitle('Speedreducer', fontsize = 14, fontweight='bold')
plt.legend(('SSA', 'MSA',"GWO","FA"))
plt.show()