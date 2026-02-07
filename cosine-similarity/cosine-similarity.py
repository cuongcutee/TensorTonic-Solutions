import numpy as np

def cosine_similarity(a, b):
    a= np.asarray(a)
    b= np.asarray(b) 
    
    dot_product = np.sum(a*b)
    az= np.sqrt(np.sum(a**2))
    bz = np.sqrt(np.sum(b**2))
    if az ==0 or bz==0:
        return float(0)
    return float(dot_product/(az*bz))
