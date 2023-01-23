Центральный момент

import numpy as np

def central_moment(sample, k):
    mean = np.mean(sample)
    central_moment = np.mean((sample - mean) ** k)
    return central_moment

with open('input.txt','r') as f:
    n,k = map(int, f.readline().split())
    sample = list(map(float, f.readline().split()))

with open('output.txt','w') as f:
    f.write(str(round(central_moment(sample, k),4)))
