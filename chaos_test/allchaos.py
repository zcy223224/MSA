from math import acos, cos, exp, sin, sqrt
import math
import numpy as np
pi=math.pi
''''''
def Logistic(start=500,dimension=30,timer=1):
    st=[]
    temp=0.152
    u=4
    i=0
    st.append(temp)
    while(i<start):
        temp=u*st[i]*(1-st[i])
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        temp=u*z[i-start]*(1-z[i-start])
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def PWLCM(start=500,dimension=30,timer=1):
    st=[]
    temp=0.2*(np.random.rand()+0.001)
    u=0.62
    i=0
    st.append(temp)
    while(i<start):
        if(st[i]<u):
            temp=st[i]/u
        else:
            temp=(1-st[i])*(1-u)
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        if(z[i-start]<u):
            temp=z[i-start]/u
        else:
            temp=(1-z[i-start])*(1-u)
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def Singer(start=500,dimension=30,timer=1):
    st=[]
    temp=0.152
    u=1.073
    i=0
    st.append(temp)
    while(i<start):
        temp=u*(7.86*st[i]-23.31*st[i]**2+28.75*st[i]**3-13.302875*st[i]**4)
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        temp=u*(7.86*z[i-start]-23.31*z[i-start]**2+28.75*z[i-start]**3-13.302875*z[i-start]**4)
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def Sine(start=500,dimension=30,timer=1):
    st=[]
    temp=0.152
    u=4
    i=0
    st.append(temp)
    while(i<start):
        temp=u/4*sin(pi*st[i])
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        temp=u/4*sin(pi*z[i-start])
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def Gaussian(start=500,dimension=30,timer=1):
    st=[]
    temp=0.152
    u=1
    i=0
    st.append(temp)
    while(i<start):
        if(st[i]==0):
            temp=0
        else:
            temp=(u/st[i])%1
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        if(z[i-start]==0):
            temp=0
        else:
            temp=(u/z[i-start])%1
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def Tent(start=500,dimension=30,timer=1):
    st=[]
    temp=0.152
    u=0.4
    i=0
    st.append(temp)
    while(i<start):
        if(st[i]<=u):
            temp=st[i]/u
        else:
            temp=(1-st[i])/(1-u)
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        if(z[i-start]<=u):
            temp=z[i-start]/u
        else:
            temp=(1-z[i-start])/(1-u)
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def Bernoulli(start=500,dimension=30,timer=1):
    st=[]
    temp=0.152
    u=0.4
    i=0
    st.append(temp)
    while(i<start):
        if(st[i]<=1-u):
            temp=st[i]/(1-u)
        else:
            temp=(st[i]-1+u)/u
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        if(z[i-start]<=1-u):
            temp=z[i-start]/(1-u)
        else:
            temp=(z[i-start]-1+u)/u
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def Chebyshev(start=500,dimension=30,timer=1):
    st=[]
    temp=0.152
    u=5
    i=0
    st.append(temp)
    while(i<start):
        temp=cos(u*acos(st[i]))
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        temp=cos(u*acos(z[i-start]))
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def Circle(start=500,dimension=30,timer=1):
    st=[]
    temp=0.152
    i=0
    st.append(temp)
    while(i<start):
        temp=st[i]+0.5-1.1/pi*sin(2*pi*st[i])%1
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        temp=z[i-start]+0.5-1.1/pi*sin(2*pi*z[i-start])%1
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def Cubic(start=500,dimension=30,timer=1):
    st=[]
    temp=0.242
    u=2.59
    i=0
    st.append(temp)
    while(i<start):
        temp=u*st[i]*(1-st[i]**2)
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        temp=u*z[i-start]*(1-z[i-start]**2)   
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def Sinusoidal(start=500,dimension=30,timer=1):
    st=[]
    temp=0.74
    u=2.3
    i=0
    st.append(temp)
    while(i<start):
        temp=u*st[i]**2*sin(pi*st[i])
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        temp=u*z[i-start]**2*sin(pi*z[i-start])
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''
def ICMIC(start=500,dimension=30,timer=1):
    st=[]
    temp=0.152
    u=70
    i=0
    st.append(temp)
    while(i<start):
        temp=sin(u/st[i])
        i+=1
        st.append(temp)
    z=[]
    z.append(st[i-1])
    while(i<dimension+start-1):
        temp=sin(u/z[i-start])
        i+=1
        z.append(temp)
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result
''''''