Дан массив чисел. Нужно заменить в нем максимальный элемент на минимальный из этого же массива. Если максимальных несколько — заменить каждый из них.

_arr = list(map(int,input().split()))
_arr =[min(_arr) if _arr[k] == max(_arr)
                 else _arr[k] 
                 for k in range(len(_arr))]
print(" ".join(list(map(str,_arr))))
