Не знаем, зачем, но заказчику необходимо разделить персонажей на две группы.

_str1=""
_str2=""
for i in range(6):
    if i%2 ==0:
        _str1 += input()+", "
    else:
        _str2 += input()+", "

print(_str1[:len(_str1)-2])
print(_str2[:len(_str2)-2])
