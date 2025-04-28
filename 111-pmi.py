import numpy as np

def compute_pmi(joint_counts, total_counts_x, total_counts_y, total_samples):
    joint_prob = joint_counts/total_samples 
    prob_x = total_counts_x/total_samples
    prob_y = total_counts_y/total_samples 
    pmi = np.log2(joint_prob/(prob_x * prob_y))
    rounded = round(pmi, 3)
    if rounded.is_integer():
        return int(rounded)
    return rounded