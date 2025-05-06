import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    if len(p) != len(q):
        return 0.
    p = np.array(p)
    q = np.array(q)
    bc = np.sum(np.sqrt(p * q))
    return -np.log(bc)