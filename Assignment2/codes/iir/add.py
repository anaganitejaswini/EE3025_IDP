import numpy as np

def add(X,Y):
  x=len(X)
  y=len(Y)
  if x==y:
    z= x+y
  elif x>y:
    y_pad=np.append(np.zeros(x-y),Y)
    z=X+y_pad
  else:
    x_pad=np.append(np.zeros(y-x),X)
    z=x_pad + Y
  return z