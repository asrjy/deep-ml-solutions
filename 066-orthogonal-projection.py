def orthogonal_projection(v, L):
    vL = [v[i] * L[i] for i in range(len(v))]
    LL = sum([L[i]**2 for i in range(len(L))])
    term = [vL[i]/LL for i in range(len(v))]
    orthogonal_projection = [term[i] * L[i] for i in range(len(v))]
    return orthogonal_projection
