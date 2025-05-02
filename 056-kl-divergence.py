import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
    kld = np.log(sigma_q/sigma_p)  
    kld += ((sigma_p**2) + (mu_p - mu_q)**2)/(2 * (sigma_q**2))
    kld -= 0.5
    return kld
