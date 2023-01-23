Поворот матрицы

def transposed(_arr):
    _matrix = [[*row] for row in zip(*_arr)]
    return _matrix

def print_matrix(_arr):
    for i in _arr:
        print(" ".join(list(map(str,i))))
        
N,M,k = map(int, input().split())
_arr = []
for i in range(N):
    _arr.append(input().split())
new_arr = _arr
k =k%4
if k ==0:
    k = 4
    
for i in range(k):
    new_arr = transposed(reversed(new_arr))
print_matrix(new_arr)
