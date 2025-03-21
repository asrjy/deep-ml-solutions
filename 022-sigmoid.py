import math

def sigmoid(z: float) -> float:
    result = round(1/(1 + math.exp(-z)), 4)
    return result