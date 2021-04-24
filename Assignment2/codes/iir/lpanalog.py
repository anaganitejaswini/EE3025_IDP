import numpy as np
import matplotlib.pyplot as plt
from cheb import *
#If using termux
import subprocess
import shlex
#end if

epsilon = 0.4
N = 4

#Analytically obtaining the roots of the Chebyschev polynomial
#in the left half of the complex plane

beta = ((np.sqrt(1+epsilon**2)+ 1)/epsilon)**(1/N)
r1 = (beta**2-1)/(2*beta)
r2 = (beta**2+1)/(2*beta)

#Obtaining the polynomial approximation for the low pass
#Chebyschev filter to obtain a stable filter
u = np.array([1])
for n in range(0,int(N/2)): #n = 0:(N/2)-1;
    phi = np.pi/2 + (2*n+1)*np.pi/(2*N)
    v = [1,-2*r1*np.cos(phi),r1**2*np.cos(phi)**2+r2**2*np.sin(phi)**2]
    p = np.convolve(v,u)
    u = p

p1 = epsilon**2*np.convolve(cheb(N),cheb(N)) + np.concatenate([np.zeros(2*N),np.array([1])])
G = abs(np.polyval(p,1j))/np.sqrt(1+epsilon**2)
Omega = np.arange(0,2.01,0.01) #0:0.01:2
H_stable = abs(G/np.polyval(p,1j*Omega))
H_cheb = abs(np.sqrt(1/np.polyval(p1,1j*Omega)))
plt.figure()
plt.plot(Omega,H_stable,'o',label='Design')
plt.plot(Omega,H_cheb,label='Specification')
plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,LP}(j\Omega)|$')
plt.legend()
plt.savefig('../figs/iir/AnalogLP_cheb.eps')
plt.savefig('../figs/iir/AnalogLP_cheb.pdf')
subprocess.run(shlex.split("termux-open ../figs/iir/AnalogLP_cheb.pdf"))
#else
#plt.show()