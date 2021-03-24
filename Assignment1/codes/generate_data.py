import soundfile as sf
import numpy as np
from scipy import signal

#If using termux
import subprocess
import shlex

#Reading the soundfile 
input_signal, fs = sf.read('../data/Sound_Noise.wav')
order = 4
cutoff_freq = 4000
n = int(len(input_signal))
n = int(2 ** np.floor(np.log2(n)))
f = open("../data/x.dat", "w") #Creating a dat file with input data
for i in range(n):
    f.write(str(input_signal[i]) + "\n")
f.close()
