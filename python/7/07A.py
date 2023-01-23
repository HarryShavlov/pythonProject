Требуется написать программу, которая вычисляет среднее арифметическое заданной выборки.
При решении задачи необходимо использовать библиотеку numpy.

import numpy

with open("input.txt", "r") as f:
    s = list(map(float,f.read().split()))
    N = int(s[0]+1)
with open("output.txt","w") as f:
    f.write(str(float('{:.3f}'.format(numpy.mean(s[1:N])))))
