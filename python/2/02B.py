
#Время отправления и время прибытия поезда задаются в виде Ч М, где Ч - час от 0 до 23, М - минута от 0 до 59. 
#Время в пути задаётся аналогично в формате Ч М, где Ч - количество часов от 0 до 999, а М - количество минут от 0 до 59.
#Требуется по данному времени отправления и времени в пути вычислить время прибытия поезда (возможно, в другие сутки).

with open("input.txt","r") as f:
    myList = [line.split() for line in f]
    v_otp = myList[0]
    v_put = myList[1]
min_pri = int(v_put[1]) +int(v_otp[1])
ch_pri = int(v_put[0]) +int(v_otp[0])
if min_pri >= 60:
    min_pri -=60
    ch_pri +=1
while ch_pri >=24:
    ch_pri -=24
with open("output.txt","w") as f:
    f.write(str(ch_pri)+" "+str(min_pri))
