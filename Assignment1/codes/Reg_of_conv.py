import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from matplotlib import patches
#If using termux
import subprocess
import shlex
#end if

#co-efficients
a = np.array([1.,         -2.5194645,   2.56083711, -1.20623537,  0.22012927])
b = np.array([0.00345416, 0.01381663, 0.02072494, 0.01381663, 0.00345416])

poles=np.poly1d(a).r
print("Poles: ", poles)
pr = np.real(poles)
pi = np.imag(poles)
zeros=np.poly1d(b).r
print("Zeros: ",zeros)
zr = np.real(zeros)
zi = np.imag(zeros)

x = np.linspace(-2,2,100)
ax = plt.subplot(111)
# Add unit circle and zero axes    
unit_circle = patches.Circle((0,0), radius=1, fill=False,color='black', ls='dashed')
ax.add_patch(unit_circle)

y1 = np.sqrt(16-x**2)
y2 = -np.sqrt(16-x**2)
plt.fill_between(x, y1, y2, color='#539ecd')

# Add circle passing through max abs(poles) and zero axes    
req_circle = patches.Circle((0,0), radius=np.max(np.abs(poles))
			, fill=True,color='white',ls='solid')
ax.add_patch(req_circle)
boundary = patches.Circle((0,0), radius=np.max(np.abs(poles))
			, fill=False,color='black',ls='solid')
ax.add_patch(boundary)

plt.plot(zr,zi,'o',markersize=7,color='red')
plt.plot(pr,pi,'x',color='red',markersize=7)
plt.text(-0.1,0,"z=0")
plt.text(0.3,0.75,"ROC")
plt.text(0,1.1,"|z|=1")
plt.title('Pole zero plot in z plane with ROC |z| > 0.811')
plt.xlabel('real')
plt.ylabel('Imaginary')
plt.grid()
plt.axis('scaled')
plt.axis([-1.5,1.5,-1.5,1.5])
#If using termux
plt.savefig('../figs/roc.pdf')
plt.savefig('../figs/roc.eps')
subprocess.run(shlex.split("termux-open ../figs/roc.pdf"))

#else
#plt.show()
