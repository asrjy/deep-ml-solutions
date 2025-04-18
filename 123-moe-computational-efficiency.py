def compute_efficiency(n_experts, k_active, d_in, d_out):
    flops_dense = n_experts * d_in * d_out
    flops_moe = k_active * d_in * d_out 
    savings_percent = ((flops_dense - flops_moe)/flops_dense) * 100
    return savings_percent