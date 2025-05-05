import numpy as np 

def elu(x: float, alpha: float = 1.0) -> float:
    if x > 0:
        val = float(x)
        return val
    else:
        val = alpha * (np.exp(x) - 1)
        return round(val, 4)