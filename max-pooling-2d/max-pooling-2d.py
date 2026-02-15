import numpy as np
def max_pooling_2d(X, pool_size):
    X = np.asarray(X)
    H,W = X.shape
    h = H//pool_size
    w = W//pool_size
    matrix = np.zeros((h,w))
    for i in range(h):
      for j in range(w):
        matrix[i][j] = np.max(X[pool_size*i:pool_size*i + pool_size,pool_size*j: pool_size*j + pool_size])
    return matrix.tolist()