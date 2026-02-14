import numpy as np


def batch_norm_forward_2D(x,gamma,beta,eps = 1e-5):
    x_mean = np.mean(x,axis = 0,keepdims = True)
    x_var = np.var(x,axis = 0,keepdims = True)
    x_nor = ( x - x_mean)/(np.sqrt(x_var+eps))
    return x_nor * gamma + beta
def batch_norm_forward_4D(x,gamma,beta,eps = 1e-5):
    N,C,H,W = x.shape
    gamma = gamma.reshape((1,C,1,1))
    beta = beta.reshape((1,C,1,1))
    x_mean = np.mean(x,axis=(0,2,3),keepdims = True)
    x_var = np.var(x,axis=(0,2,3),keepdims = True)
    x_nor = ( x - x_mean)/(np.sqrt(x_var+eps))
    return x_nor * gamma + beta
def batch_norm_forward(x, gamma, beta, eps=1e-5):
    x = np.asarray(x)
    gamma = np.asarray(gamma)
    beta = np.asarray(beta)
    if x.ndim == 2:
        return batch_norm_forward_2D(x, gamma,beta,eps= eps)
    else:
        return batch_norm_forward_4D(x,gamma,beta,eps=eps)
