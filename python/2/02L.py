Аня очень хорошо разбирается в грибах. Грибы бывают разные. 
Опята, лисички. сыроежки, подосиновики, подберезовики, обабки, маслята, оленьи рожки, поганки (ядовитые). 
Boletus edulis (белые грибы) — самые хорошие. Нужно посчитать, сколько Boletus edulis собрала Аня.

N = int(input())
_str=""
for i in range(N):
    _str+=input()+","
array = list(map(str, _str.split(",")))
j=0
for i in range(len(array)):
    if array[i].lower() == "boletus edulis":
        j+=1
print(j)

