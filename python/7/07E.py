Метод скользящего взвешенного среднего

import numpy as np

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    weights = np.array(f.readline().split(),dtype=int)
    arr = np.array(f.readline().split(),dtype=float)

with open("output.txt", "w") as f:
    weighted_average = np.convolve(arr, weights[::-1], 'valid') / weights.sum()
    f.write(' '.join([str(int(value*1000) if value == int(value) else f'{value:.3f}' ).rstrip('0').rstrip('.') for value in weighted_average]))
