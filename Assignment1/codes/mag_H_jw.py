import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if



x,fs = sf.read('../data/Sound_Noise.wav')
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq

b,a = signal.butter(order,Wn,'low')
omega = np.linspace(-np.pi,np.pi,len(x))
z = np.exp(1j * omega)  # z= e^{jw}


def H(z,num_coeffs,den_coeffs):
    Num = np.polyval(num_coeffs,pow(z,-1))
    Den = np.polyval(den_coeffs,pow(z,-1))
    return Num/Den

H = H(z,b,a)
#subplots
plt.plot(omega,abs(H))
plt.title('Magnitude of Impulse Frequency Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(j\omega)|$')
plt.grid()
#If using termux
plt.savefig('../figs/mag_H(jw).pdf')
plt.savefig('../figs/mag_H(jw).eps')
subprocess.run(shlex.split("termux-open ../figs/mag_H(jw).pdf"))

#else
#plt.show()
