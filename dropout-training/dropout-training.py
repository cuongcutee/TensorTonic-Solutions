import numpy as np

def dropout(x, p=0.5, rng=None):
    scale = 1/(1-p)
    x = np.asarray(x)
    if rng!= None:
        pi = rng.random(x.shape)
    else:
        pi = np.random.random(x.shape)
    scale_real = (pi<(1-p))*scale
    return(x*scale_real,scale_real)