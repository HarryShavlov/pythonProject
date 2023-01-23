Требуется написать программу, которая выводит таблицу умножения чисел от 1 до n.

N = int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        print(f"{i} * {j} = "+str(i*j))
