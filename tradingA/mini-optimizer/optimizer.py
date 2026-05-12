import numpy as np

def run_optimizer(values):
    arr = np.array(values)
    mean = np.mean(arr)
    std = np.std(arr)
    return {
        "input": values,
        "mean": round(mean, 2),
        "std_dev": round(std, 2),
        "optimized": list(arr / (std + 1e-6))
    }
