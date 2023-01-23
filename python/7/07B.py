Требуется написать программу, которая вычисляет среднее гармоническое заданной выборки.
При решении задачи необходимо использовать библиотеку numpy.

import numpy

with open("input.txt", "r") as f:
    s = list(map(float,f.read().split()))
    N = int(s[0]+1)
with open("output.txt","w") as f:
    s1 = [1 /s[i] for i in range(1,len(s))]
    hmean = (N-1) / numpy.sum(s1)
    f.write(str(float('{:.3f}'.format(hmean))))
