Гистограмма 

import numpy as np

with open("input.txt","r") as f:
    n = int(f.readline())
    data = list(map(float, f.read().split()))

k = 1 + int(np.log2(n))

hist, bins = np.histogram(data, bins=k)
s = ""
for count in hist:
    s += str(count) +' '

with open("output.txt", "w") as f:
    f.write(s[:len(s)-1])
