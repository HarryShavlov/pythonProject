Требуется написать программу, которая поэлементно складывает два массива.


N = int(input())
arr1 = list(map(int, input().split()))
arr2 =list(map(int, input().split()))

_str = ""
for i in range(N):
    _str+=str(arr1[i]+arr2[i])+" "
print(_str)
