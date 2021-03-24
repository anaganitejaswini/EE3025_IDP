import soundfile as sf
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

#Reading the soundfile 
input_signal, fs = sf.read('../data/Sound_Noise.wav')
sampl_freq = fs
order = 4
n = int(len(input_signal))
n = int(2 ** np.floor(np.log2(n)))

xn = np.loadtxt('../data/x.dat')
yn = np.loadtxt('../data/yn.dat')

print("Max of x[n] is "+str(np.max(xn))+" ,Min of x[n] is "+str(np.min(xn)))
print("Max of y[n] is "+str(np.max(yn))+" ,Min of y[n] is "+str(np.min(yn)))

t = np.linspace(0, n-1,n)

#Writing the filtered sound data into a wav file
sf.write('../data/Sound_de.wav', yn, sampl_freq)

plt.subplot(2,1,1)
plt.plot(t,xn)
plt.title("Input and Output from the difference equation")
plt.xlabel("n")
plt.ylabel("x(n)")

plt.subplot(2,1,2)
plt.plot(t,yn)
plt.xlabel("n")
plt.ylabel("y(n)")

#if using termux
plt.savefig('../figs/xn_yn.eps')
plt.savefig('../figs/xn_yn.pdf')

subprocess.run(shlex.splilt("termux-open ../figs/xn_yn.pdf"))

#else
#plt.show()

