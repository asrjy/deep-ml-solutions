import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    max_score = np.max(scores)
    log_ = 0
    for score in scores:
        log_ += np.exp(score - max_score)
    log_ = np.log(log_)
    log_softmax = [(i - max_score - log_) for i in scores]
    return log_softmax