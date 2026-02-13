import numpy as np

def matrix_trace(A):
   A = np.asarray(A)
   count = 0
   for i in range(len(A)):
        count += A[i][i]
   return count

