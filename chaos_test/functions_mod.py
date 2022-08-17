from math import cos, exp, sin, sqrt
import math
import numpy as np
pi=math.pi
'''工具函数'''
def overlimit(limit,num):
    if(num>limit):
        return limit
    elif(num<-limit):
        return -limit
    else:
        return num
        
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
'''以下是要测试的函数--------------------------------------------------------------------------------'''


'''最值基本不是原点'''
'''Ackley函数,最值x[i]-i*0.5,0.一般a = 20, b = 0.2 and c = 2π'''
def Ackley(x):
    c=2*pi
    length=int(len(x)-1)
    i=0
    temp0=0.0
    temp1=0.0
    result=0.0
    while(i<length):
        temp0+=float(x[i]-i*0.5)**2
        i+=1
    temp0=-0.2*sqrt(temp0/length)

    temp0=-20*exp(temp0)
    i=0
    while(i<length):
        temp1+=cos(float(x[i]-i*0.5)*c)
        i+=1
    temp1=exp(temp1/length)
    result=temp0-temp1+20+exp(1)
    return result

'''Perm函数,最值{1,1/2,1/3......1/dimension},0'''
def Perm(x):
    result=0
    length=int(len(x)-1)
    i=0
    while(i<length):
        j=0
        temp1=0
        while(j<length):
            temp1+=(j+1.5)*(float(x[j])**(i+1)-1/(j+1)**(i+1))
            j+=1
        result+=temp1**2
        i+=1
    return result

'''Trid函数,最值Xi=i(d+1-i)，-d(d+4)(d-1)/6,此处为- 4,930'''
def Trid(x):
    result=0
    length=int(len(x)-1)
    i=1
    temp0=0
    temp1=0
    while(i<length):
        temp0+=(float(x[i])-1)**2
        temp1+=float(x[i])*float(x[i-1])
        i+=1
    temp0+=(float(x[0])-1)**2
    result=temp0-temp1
    return result

'''Zakharov函数,最值x[i]-i*0.2,0'''
def Zakharov(x):
    result=0
    length=int(len(x)-1)
    i=0
    temp0=0
    temp1=0
    while(i<length):
        temp0+=float(x[i]-i*0.2)**2
        temp1+=float(x[i]-i*0.2)*0.5*(i+1)
        i+=1
    result=temp0+temp1**2+temp1**4
    return result

'''Powell函数,最值-i,0'''
def Powell(x):
    result=0
    length=int((len(x)-1)/4)
    i=0
    temp0=0
    temp1=0
    temp2=0
    temp3=0
    while(i<length):
        temp0=float(x[4*i]-i*0.1)+10*float(x[4*i+1]-i*0.1)
        temp1=float(x[4*i+2]-i*0.1)-float(x[4*i+3]-i*0.1)
        temp2=float(x[4*i+1]-i*0.1)-2*float(x[4*i+2]-i*0.1)
        temp3=float(x[4*i]-i*0.1)-float(x[4*i+3]-i*0.1)
        result+=temp0**2+5*temp1**2+temp2**4+10*temp3**4
        i+=1
    return result



'''以下是原论文中出现的非固定维函数'''
'''F1函数,最值x[i]-i,0'''
def F1(x):
    result=0
    length=int(len(x)-1)
    i=0
    while(i<length):
        result+=float(x[i]-i)**2
        i+=1
    return result

'''F2函数,最值x[i]-i*0.2,0'''
def F2(x):
    result=0
    length=int(len(x)-1)
    i=0
    temp0=0
    temp1=1
    while(i<length):
        temp0+=abs(float(x[i]-i*0.2))
        temp1*=abs(float(x[i]-i*0.2))
        i+=1
    result=temp0+temp1
    return result

'''F3函数,最值x[j]-j,0'''
def F3(x):
    result=0
    length=int(len(x)-1)
    i=0
    temp0=0
    while(i<length):
        temp0=0
        j=0
        while(j<=i):
            temp0+=float(x[j]-j)
            j+=1
        result+=temp0**2
        i+=1
    return result

'''F4函数,最值x[i]-i,0'''
def F4(x):
    length=int(len(x)-1)
    i=0
    temp0=0
    while(i<length):
        if(abs(float(x[i]-i))>temp0):
            temp0=abs(float(x[i]-i))
        i+=1
    return temp0

'''F5函数,最值x[i]-i*0.3,0'''
def F5(x):
    result=0
    temp0=0
    temp1=0
    length=int(len(x)-1)
    i=0
    while(i<length-1):
        temp0=100*(float(x[i+1]-i*0.3-0.3)-float(x[i]-i*0.3)**2)**2
        temp1=(float(x[i]-i*0.3)-1)**2
        result+=temp0+temp1
        i+=1
    return result

'''F6函数,最值x[i]-i,0'''
def F6(x):
    result=0
    length=int(len(x)-1)
    i=0
    temp0=0
    while(i<length):
        temp0=int(float(x[i]-i))
        result+=temp0**2
        i+=1
    return result

'''F7函数,最值x[i]-i*0.01,0'''
def F7(x):
    result=0
    length=int(len(x)-1)
    i=0
    while(i<length):
        result+=i*float(x[i]-i*0.01)**4
        i+=1
    return result+np.random.rand()

'''F8函数,最值?，-418.9829 n,在这里n=30,即-12,569.487'''
def F8(x):
    result=0
    length=int(len(x)-1)
    i=0
    temp0=0
    while(i<length):
        temp0=sin(sqrt(abs(float(x[i]))))
        result-=temp0*float(x[i])
        i+=1
    return result

'''F9函数,最值x[i]-i*0.05,0'''
def F9(x):
    result=0
    length=int(len(x)-1)
    i=0
    temp0=0
    while(i<length):
        temp0=float(x[i]-i*0.05)**2-10*cos(2*pi*float(x[i]-i*0.05))+10
        result+=temp0
        i+=1
    return result

'''F10函数,最值x[i]-i,0'''
def F10(x):
    result=0
    length=int(len(x)-1)
    i=1
    temp0=0
    while(i<length):
        temp0+=float(x[i]-i)**2
        i+=1
    result=float(x[0])**2+1000000*temp0
    return result

'''F11函数,最值x[i]-i*10,0'''
def F11(x):
    result=0
    length=int(len(x)-1)
    i=0
    temp0=0
    temp1=1
    while(i<length):
        temp0+=float(x[i]-i*10)**2
        temp1*=cos(float(x[i]-i*10)/(sqrt(i+1)))
        i+=1
    result=temp0/4000-temp1+1
    return result

'''F12函数,最值-1,-i,0'''
def F12(x):
    result=0
    length=int(len(x)-1)
    i=0
    tempu=0
    while(i<length):
        if(float(x[i]-i)>10):
            tempu+=100*(float(x[i]-i)-10)**4
        elif(float(x[i]-i)<(-10)):
            tempu+=100*(-float(x[i]-i)-10)**4
        else:
            tempu+=0
        i+=1
    temp0=0
    i=0
    yi=0
    yi1=0
    while(i<length-1):
        yi1=1.25+float(x[i+1]-i-1)/4
        yi1*=pi
        yi1=sin(yi1)**2
        yi1=1+10*yi1
        yi=0.25+float(x[i]-i)/4
        yi=yi**2
        temp0+=yi*yi1
        i+=1
    temp2=temp0+10*sin(pi*(1.25+float(x[0])/4))+(0.25+float(x[length-1]-length+1)/4)**2
    result=temp2*pi/length+tempu
    return result