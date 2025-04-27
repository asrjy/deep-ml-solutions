def phi_corr(x: list[int], y: list[int]) -> float:
    x_00, x_01, x_10, x_11 = 0, 0, 0, 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == 1 and y[i] == 1:
                x_11 += 1
            elif x[i] == 0 and y[i] == 0:
                x_00 += 1
            elif x[i] == 1 and y[i] == 0:
                x_10 += 1
            else:
                x_01 += 1
    val = (x_00 * x_11) - (x_01 * x_10)
    val /= ((x_00 + x_01) * (x_10 + x_11) * (x_00 + x_10) * (x_01 + x_11))**0.5
    return round(val,4)