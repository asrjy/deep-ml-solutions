def grad_val(x):
    val = (4 * x**3) - (9 * x**2)
    return val 

def find_treasure(start_x: float) -> float:
    lr = 0.01
    tolerance = 1e-6
    n_epochs = 1000

    if start_x < 0:
        old_pos = 1.0
    else: 
        old_pos = start_x


    for i in range(n_epochs):
        new_pos = old_pos - (lr * grad_val(old_pos))
        if abs(new_pos - old_pos) < tolerance:
            old_pos = new_pos
            break
        old_pos = new_pos
    
    return new_pos

