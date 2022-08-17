from math import gamma, sin, sqrt
import numpy as np

pi=3.141592654
def fly(idomain,dimension):
    beta=1.5
    u = (gamma(1+beta)*sin(pi*beta/2)/(gamma((1+beta)/2)*beta*2**((beta-1)/2)))**(1/beta)
    u = np.random.randn()*u
    v = np.random.randn()
    s = u/(abs(v))**(1/beta)
    steplength=abs(s*idomain)
    RatioDimension=np.random.rand(dimension)*2-1
    Ratiolength=0
    for levyvar in RatioDimension:
        Ratiolength+=levyvar**2
    Ratiolength=sqrt(Ratiolength)
    levyi=0
    while(levyi<dimension):
        RatioDimension[levyi]*=steplength/Ratiolength
        levyi+=1
    return RatioDimension
