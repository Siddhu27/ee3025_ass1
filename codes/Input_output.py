import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,1,2,4,3,1])
N=20
x=np.pad(x,(0,N-len(x)),'constant')
a=np.arange(N)
y=np.zeros(N)
for i in range(N):
	y[i]=x[i]+x[i-2]-0.5*y[i-1]
plt.figure(1)
plt.title("Input")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.stem(a,x)
plt.figure(2)
plt.title("Bounded Output")
plt.xlabel("n")
plt.ylabel("y(n)")
plt.stem(a,y)
plt.show()	
