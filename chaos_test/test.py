from matplotlib import pyplot as plt
from allchaos import Logistic,PWLCM,Singer,Sine,Gaussian,Tent,Bernoulli,Chebyshev,Circle,Cubic,Sinusoidal,ICMIC


n=10000
Y=ICMIC(500,n,1)
X=range(n)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.scatter(X, Y, c='b', s=0.1,alpha=1)
plt.show()