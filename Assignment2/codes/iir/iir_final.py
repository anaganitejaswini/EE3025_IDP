import numpy as np
from lp_stable_cheb import *
from lpbp import *
from bilin import * 
import matplotlib.pyplot as plt
import struct
#If using termux
import subprocess
import shlex
#end if


epsilon = 0.4
N = 4
p,G_lp = lp_stable_cheb(epsilon,N)
Omega_0 = 0.4594043442925196
B = 0.09531188712133376
Omega_p1 = 0.5095254494944288
Omega_L = np.arange(0,2+0.01,0.01)
H_analog_lp = G_lp*abs(1.0/np.polyval(p,1j*Omega_L))
plt.figure(1)
plt.plot(Omega_L, H_analog_lp)
#plt.show()

[num,den,G_bp] = lpbp(p,Omega_0,B,Omega_p1)
Omega = np.arange(-0.65,0.65+0.01,0.01) 
H_analog_bp = G_bp*abs(np.polyval(num,1j*Omega)/np.polyval(den,1j*Omega))
plt.figure(2)
plt.ylabel('$|H_{a,BP}(j\Omega)|$')
plt.plot(Omega,H_analog_bp)
plt.savefig('../figs/iir/BP_analog.eps')
plt.savefig('../figs/iir/BP_analog.pdf')
#subprocess.run(shlex.split("termux-open ../figs/iir/BP_analog.pdf"))
#plt.show()

dignum,digden,G = bilin(den,Omega_p1)
omega = np.arange(-2*np.pi/5,(np.pi/1000)+2*np.pi/5, (np.pi/1000))
H_dig_bp = G*abs(np.polyval(dignum,np.exp(-1j*omega))/np.polyval(digden,np.exp(-1j*omega)))
plt.figure(3)
plt.plot(omega/np.pi,H_dig_bp)
plt.ylabel('$|H_{d,BP}(j\Omega)|$')
plt.savefig('../figs/iir/BP_digital.eps')
plt.savefig('../figs/iir/BP_digital.pdf')
#subprocess.run(shlex.split("termux-open ../figs/iir/BP_digital.pdf"))
#plt.show()

iir_num = G*dignum
iir_den = digden

G = np.array([G])
np.savetxt('dignum.dat',dignum,delimiter=',')
np.savetxt('G.dat',G,delimiter=',')
np.savetxt('digden.dat',digden,delimiter=',')
np.savetxt('iir_num.dat',iir_num,delimiter=',')
np.savetxt('iir_den.dat',iir_den,delimiter=',')
