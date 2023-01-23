 Метод скользящего среднего 
  
 import numpy as np


def moving_avg(x, n):
 cumsum = np.cumsum(np.insert(x, 0, 0))
 return (cumsum[n:] - cumsum[:-n]) / float(n)

with open("input.txt","r") as f:
    lines = f.readlines()
    n, m = map(int, lines[0].split())
    x = list(map(float,lines[1].split()))
with open("output.txt","w") as f:
    a = moving_avg(x,m).tolist()
    f.write(" ".join(map(str,[round(a[i],4) for i in range(len(a))])))
