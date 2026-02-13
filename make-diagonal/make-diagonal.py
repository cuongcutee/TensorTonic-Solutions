import numpy as np

def make_diagonal(v):
    v = np.asarray(v)
    n = len(v)
    matrix = np.zeros((n,n))
    for i in range(n):
        matrix[i][i] = v[i]
    return np.asarray(matrix)