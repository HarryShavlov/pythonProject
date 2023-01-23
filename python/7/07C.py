Требуется написать программу, которая вычисляет средние арифметическое, гармоническое и геометрическое заданного вариационного ряда.
При решении задачи необходимо использовать библиотеку numpy.


import numpy

with open("input.txt", "r") as f:
    s = int(f.readline())
    _str = []
    for i in range(s):
        _str.append(list(map(float,f.readline().split())))
_s =[]
for j in range(len(_str)):
    for i in range(int(_str[j][1])):
        _s.append(_str[j][0])

s1 = [1 / _s[i] for i in range(len(_s))]
hmean = len(_s) / numpy.sum(s1)
a = numpy.log(_s)
gmean = numpy.exp(a.mean())
with open("output.txt","w") as f:
    f.write(str(float('{:.3f}'.format(numpy.mean(_s)))) + " " + str(float('{:.3f}'.format(hmean)))+ " " + str(float('{:.3f}'.format(gmean))))
