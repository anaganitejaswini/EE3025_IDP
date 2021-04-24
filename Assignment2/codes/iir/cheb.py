import numpy as np
#If using termux
import subprocess
import shlex
#end if

def cheb(N):
  v=np.array([1,0])
  u= np.array([1])

  if N==0:
    w=u
  elif N==1:
    w=v
  else:
    for _ in range(N-1):
      p=np.convolve(np.array([2,0]), v , mode='full')
      m= len(p)
      n=len(u)
      w= p + np.append(np.zeros(m-n),u)
      u=v
      v=w
  return w