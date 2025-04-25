import math

def binomial_probability(n, k, p):
    nck = math.factorial(n)/(math.factorial(n-k) * math.factorial(k))
    p_k = p ** k
    q_k = (1 - p)**(n - k)

    return round(nck * q_k * p_k, 5)