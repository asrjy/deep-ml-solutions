import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
    if (len(data) == 0) or degree < 0:
        return []
    return [[i**j for j in range(degree+1)] for i in data]