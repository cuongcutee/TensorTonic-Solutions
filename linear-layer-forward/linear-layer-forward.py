def linear_layer_forward(X, W, b):
    X = np.asarray(X,dtype =float)
    W = np.asarray(W,dtype =float)
    b = np.asarray(b,dtype =float)
    return (X@W + b).tolist()