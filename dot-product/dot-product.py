import numpy as np

def dot_product(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    
    return float(np.sum(x*y))
    