import numpy as np
def check_list(matrix):
    if not isinstance(matrix,list):
        return False
    if len(matrix) == 0:
        return False
    if not all(isinstance(row,list) for row in matrix):
        return False
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        return False
    for row in matrix:
        for x in row:
            if not isinstance(x,(int, float, complex, bool)):
                return False
    return True


def calculate_eigenvalues(matrix):
    if check_list(matrix) == False:
        return None
    matrix = np.asarray(matrix)
    return np.linalg.eigvals(matrix) 