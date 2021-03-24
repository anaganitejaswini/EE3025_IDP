import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


#If using termux
import subprocess
import shlex

input_signal, fs = sf.read('../data/Sound_Noise.wav')

yn= np.loadtxt('../data/ifft_y.dat')

n = len(yn)

sf.write('../data/Sound_ifft.wav', yn, fs)

plt.plot(yn)
plt.grid()
plt.xlabel("n")
plt.ylabel("y(n)")
plt.title("y(n) obtained through performing ifft(fft(Y))")

#if using termux
plt.savefig('../figs/ifft_yn.eps')
plt.savefig('../figs/ifft_yn.pdf')

#subprocess.run(shlex.splilt("termux-open ../figs/ifft_yn.pdf"))

#else
plt.show()
