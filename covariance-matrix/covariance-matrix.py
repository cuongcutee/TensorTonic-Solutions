import numpy as np

def covariance_matrix(X):
    try:
        X = np.asarray(X)
    except:
        return None
    dim = X.ndim
    
    if dim != 2:
        return None
    H,W = X.shape
    if H<2 :
        return None
    N = len(X)
    X_mean = np.mean(X,axis = 0,keepdims = True)
    X_center = X - X_mean
    return np.transpose(X_center)@ X_center/(N-1)