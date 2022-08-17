import numpy as np
import matplotlib.pyplot as plt
''''''
def PWLCM(start,dimension,timer=1):
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
    result=[]
    i=1
    for var in z:
        i=np.random.rand()-0.5
        if(i>=0):
            result.append(var*timer)
        else:
            result.append(-var*timer)
    return result

'''  
n=10000
Y=PWLCM(5000,n)
X=range(n)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.scatter(X, Y, c='b', s=0.1,alpha=1)
Individual=PWLCM(10,10,10)
print(Individual)
plt.show()
'''