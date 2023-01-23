Транспонирование квадратной матрицы

N = int(input())
_arr = []
for i in range(N):
    _arr.append((input()).split())
_newArr = [[0 for j in range(len(_arr))] for i in range(len(_arr[0]))]
for i in range(len(_arr)):
    for j in range(len(_arr[0])):
        _newArr[j][i]=_arr[i][j]
for i in range(len(_newArr)):
    print(" ".join(_newArr[i]))
