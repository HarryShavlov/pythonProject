Дан массив чисел. Необходимо удалить элементы, за которыми в этом массиве следует ноль.

_arr = input().split()

_newarr = [ _arr[i] for i in range(len(_arr)-1) if _arr[i+1] != "0"]
if _arr[len(_arr)-1] !=0:
    _newarr.append(_arr[len(_arr)-1])
print(" ".join(_newarr))
