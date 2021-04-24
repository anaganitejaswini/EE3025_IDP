
import numpy as np

def lp_stable_cheb(epsilon,N):
    beta = ((np.sqrt(1+epsilon**2)+ 1)/epsilon)**(1.0/N)
    r1 = (beta**2-1)/(2*beta)
    r2 = (beta**2+1)/(2*beta)
    u = np.array([1])
    for n in range(0,int(N/2)):
        phi = np.pi/2 + (2*n+1)*np.pi/(2*N)
        v =  np.array([1, -2*r1*np.cos(phi), r1**2*(np.cos(phi))**2+r2**2*(np.sin(phi))**2])
        p = np.convolve(v,u)
        u = p
    G = abs(np.polyval(p,1j))/np.sqrt(1+epsilon**2)
    return p,G