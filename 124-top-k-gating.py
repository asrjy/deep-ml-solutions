import numpy as np

def softplus(x: float) -> float:
    val = np.log(1 + np.exp(x))
    return val

def softmax(x):
    val = np.exp(x)/np.sum(np.exp(x))
    return val

def noisy_topk_gating(
    X: np.ndarray,
    W_g: np.ndarray,
    W_noise: np.ndarray,
    N: np.ndarray,
    k: int
) -> np.ndarray:
    """
    Args:
        X: Input data, shape (batch_size, features)
        W_g: Gating weight matrix, shape (features, num_experts)
        W_noise: Noise weight matrix, shape (features, num_experts)
        N: Noise samples, shape (batch_size, num_experts)
        k: Number of experts to keep per example
    Returns:
        Gating probabilities, shape (batch_size, num_experts)
    """
    H_base = X @ W_g
    H_noise = X @ W_noise
    H = H_base + (N * softplus(H_noise))
    batch_size, num_experts = H.shape
    out = np.zeros_like(H)
    for i in range(batch_size):
        top_k_indices = np.argpartition(H[i], -k)[-k:]
        out[i, top_k_indices] = softmax(H[i, top_k_indices])
    return out