import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    position  =np.arange(seq_len).reshape(-1,1)
    i = np.arange(d_model)
    freq =1/ base **((2*(i//2))/d_model).reshape(1,-1)
    matrix = np.matmul(position,freq)
    pe = np.zeros(matrix.shape)
    pe[:,0::2] = np.sin(matrix[:,0::2])
    pe[:,1::2] = np.cos(matrix[:,1::2])
    return pe
    
            
        
        