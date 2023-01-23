Петя написал на заборе N цифр. 
Когда Вася увидел то, что натворил Петя, он решил посчитать, сколько раз написана каждая цифра.
Напишите программу, принимающую на вход список цифр, которые написал Вася, и выводящую для каждой цифры, сколько раз она встречается в списке

with open("input.txt", "r") as f:
    arr = f.readlines()
N=int(arr[0])+1
_str = "".join(arr[1:N])
_ans =[]
for i in range(10):
    _ans.append(_str.count(f"{i}"))
if len(_ans) <10:
    for i in (len(_ans),10):
    	_ans.append("0")
_ans =_ans[1:]+_ans[:1]
_str = " ".join(str(x) for x in _ans)
with open("output.txt", "w") as f:
    f.write(_str)
