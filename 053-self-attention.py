import numpy as np

def softmax(X):
    exp_x = np.exp(X)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

def compute_qkv(X, W_q, W_k, W_v):
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V

def self_attention(Q, K, V):
    d_k = K.shape[-1]
    attn = (np.dot(Q, K.T))/(d_k ** 0.5)
    attn = softmax(attn)
    attn = np.dot(attn, V)
    return attn