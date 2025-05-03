import numpy as np 
def descriptive_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    c = np.bincount(data)
    mode = np.argmax(c) 
    variance = np.var(data)
    std_dev = np.std(data)
    percentiles = [np.percentile(data, 25), np.percentile(data, 50), np.percentile(data, 75)]
    iqr = percentiles[2] - percentiles[0]
    stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance,4),
        "standard_deviation": np.round(std_dev,4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }
    return stats_dict