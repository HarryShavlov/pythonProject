Дан вектор, состоящий из p чисел. Необходимо преобразовать вектор в матрицу размера 
n×m=p, состоящую из n строк и m столбцов. 
Матрица заполняется последовательно, то есть элементы вектора с 1 по m попадут в первую строку матрицы, с m+1 по 2m — во вторую строку и так далее.

n, arr = int(input()), list(map(int, input().split()))
_ = list(map(int, input().split()))
rows, cols = _[0], _[1]
ans = [[arr[i*cols+j] for j in range(cols)] for i in range(rows)]

for i in range(len(ans)):
    print(*ans[i])
