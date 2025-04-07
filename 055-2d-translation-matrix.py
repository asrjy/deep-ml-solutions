import numpy as np
def translate_object(points, tx, ty):
    translated_points = [[point[0] + tx, point[1] + ty] for point in points]
    return translated_points