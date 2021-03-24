import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

def to_complex(field):
	field = str(field)[2:]
	field = field[0 : len(field) - 1]
	return complex(field.replace('+-', '-').replace('i', 'j'))

X_k = np.loadtxt('../data/Xfft.dat', converters={0: to_complex}, dtype = np.complex128, delimiter = '\n')
H_k = np.loadtxt('../data/Hfft.dat', converters={0: to_complex}, dtype = np.complex128, delimiter = '\n')
X_k = np.fft.fftshift(X_k)
H_k = np.fft.fftshift(H_k)
n = len(X_k)

w = np.linspace(-np.pi,np.pi,n)

plt.subplot(2,1,1)
plt.plot(w,abs(X_k))
plt.grid()
plt.xlabel("$\omega$")
plt.ylabel("|X(k)|")
plt.title("FFT of x[n]")

plt.subplot(2,1,2)
plt.plot(w,abs(H_k))
plt.grid()
plt.xlabel("$\omega$")
plt.ylabel("|H(k)|")
plt.title("FFT of h[n]")

#if using termux
plt.savefig('../figs/Xk_Hk.eps')
plt.savefig('../figs/Xk_Hk.pdf')

subprocess.run(shlex.splilt("termux-open ../figs/Xk_Hk.pdf"))

#else
#plt.show()
