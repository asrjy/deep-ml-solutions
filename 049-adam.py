import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    m0, v0 = 0, 0
    for iter in range(1, num_iterations+1):
        grad_val = grad(x0)
        m0 = (beta1 * m0) + ((1 - beta1) * grad_val)
        v0 = (beta2 * v0) + ((1 - beta2) * grad_val**2)
        mt_c = m0/(1 - beta1**iter)
        vt_c = v0/(1 - beta2**iter)
        x0 -= (learning_rate * mt_c)/(np.sqrt(vt_c) + epsilon)
    return x0