def prelu(x: float, alpha: float = 0.25) -> float:
	if x > 0:
        return x
    else:
        return alpha * x