Запуск космического корабля это очень торжественное событие, требующее обратного отсчета.

N = int(input())
k=N
s='!'
for i in range(N):
    print(str(k)+s*i)
    k-=1
print("Start"+s*N)
