import numpy as np

def selu(x: float) -> float:
    """
    Implements the SELU (Scaled Exponential Linear Unit) activation function.

    Args:
        x: Input value

    Returns:
        SELU activation value
    """
    alpha = 1.6732632423543772
    scale = 1.0507009873554804
    if x > 0:
        return scale * x
    else:
        return scale * alpha * (np.exp(x) - 1)