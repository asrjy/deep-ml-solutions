import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
    shortcut = np.maximum(0, w1 @ x)
    res = w2 @ shortcut 
    res += shortcut 
    return res