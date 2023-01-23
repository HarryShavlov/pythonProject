Паша, Аня, Оля и Оргрим играют в игру, в которой нужно восстановить предложение по его словам, произнесенным в обратном порядке.

N = int(input())
_str= ""
for i in range(N):
    _str+=input()+" "
array = list(map(str, _str.split()))
i = N-1
while i>=0:
    print(array[i])
    i-=1
