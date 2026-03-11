def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    
    for i in range(steps):
        delta = 2*a*x0 + b
        x0 = x0 -lr * delta
    return float(x0)