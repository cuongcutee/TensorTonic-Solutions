import numpy as np

def pearson_correlation(X):
    try:
        X= np.asarray(X)
    except:
        return None

    N = len(X)
    X_mean = np.mean(X,axis= 0, keepdims = True)
    X_center = X - X_mean
    E = X_center.T @ X_center /(N-1)
    o= np.sqrt(np.diag(E))
    R = np.outer(o, o)
    return E/R