Требуется написать программу, которая вычисляет матрицу коэффициентов корреляции Пирсона заданных выборок.

При решении задачи необходимо использовать библиотеку numpy.

import numpy as np

with open("input.txt","r") as f:
    lines = f.readlines()
x =[]
n, m = map(int, lines[0].split())
for i in range(1, n+1):
    x.append(list(map(float,lines[i].split())))
a = (np.corrcoef(x)).tolist()
x.clear()
for i in range(len(a)):
    x.append(" ".join(map(str,[round(a[i][j],3) for j in range(len(a[i]))]))+"\n")
with open("output.txt","w") as f:
    for i in range(len(x)):
        f.write(x[i])
