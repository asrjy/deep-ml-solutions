def calculate_brightness(img):
    if len(img) == 0 or len(img[0]) == 0:
        return -1
    n_rows = len(img)
    n_cols = len(img[0])
    avg_brightness = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if (len(img[i]) != n_cols) or (img[i][j] < 0) or (img[i][j] > 255):
                return -1
            avg_brightness += img[i][j]
    return round(avg_brightness/(n_rows * n_cols), 2)
            
print(calculate_brightness([[100, 200], [50, 150]]))