import numpy as np
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

hn= np.loadtxt('../data/hn.dat')

n = len(hn)

plt.plot(np.arange(200),hn[:200])
plt.grid()
plt.xlabel("n")
plt.ylabel("h(n)")
plt.title("Impulse response from the difference equation")

#if using termux
plt.savefig('../figs/hn.eps')
plt.savefig('../figs/hn.pdf')

subprocess.run(shlex.splilt("termux-open ../figs/hn.pdf"))

#else
#plt.show()

