import math 

def swish(x: float) -> float:
    sigmoid = 1/(1+math.exp(-x))
    return x * sigmoid