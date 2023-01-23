Даны массив и список индексов (номеров элементов). Нумерация начинается с 1. 
Необходимо прибавить единицу к каждому элементу массива, индекс которого есть в списке индексов.

N,M = map(int,input().split())
_arr= input().split()
_arr_in = input().split()

_arr =[str(int(_arr[k])+1) if _arr[k] in _arr_in
                           else _arr[k] 
                           for k in range(N)]
print(" ".join(_arr))
