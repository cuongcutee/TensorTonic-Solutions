import numpy as np

def sigmoid(x):
     x = np.asarray(x)
     y = 1/(1+np.exp(-x))
     return y
    # Write code here
    