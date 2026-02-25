import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))
def train_logistic_regression(X, y, lr=0.1, steps=1000):
    X = np.asarray(X)
    y = np.asarray(y)
    H,W = X.shape
    w = np.zeros((W))
    b = 0.0
    
    for i in range(steps):
        z = X@w + b
        yi = _sigmoid(z)
        delta_w = (X.T @ (yi -y))/W
        delta_b = np.mean(yi-y)
        w = w - lr*delta_w
        b = b - lr*delta_b
    return (w,b)