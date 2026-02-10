import numpy as np

def matrix_inverse(A):
    A= np.asarray(A)
    H,W  = A.shape
    if H!=W:
        return None
    if np.linalg.det(A) ==0:
        return None
    else:
         return np.linalg.inv(A)
    