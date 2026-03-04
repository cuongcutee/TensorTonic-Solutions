import numpy as np


def pad_sequences(seqs, pad_value=0, max_len=None):
    N = len(seqs)
    L = max_len if max_len!= None else max(len(seq) for seq in seqs)
    matrix = np.zeros((N,L))
    matrix = matrix + pad_value
    for i in range(N):
        for j in range(len(seqs[i])):
            if j < L:
                matrix[i][j] = seqs[i][j]
    return matrix