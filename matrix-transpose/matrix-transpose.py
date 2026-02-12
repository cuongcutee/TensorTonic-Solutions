import numpy as np

def matrix_transpose(A):
    rows = len(A)
    cols = len(A[0])
    B = [[0]*rows for _ in range(cols)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]
    return np.array(B)

    
