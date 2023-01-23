Экстраполяция

import math

def calc(x):
    return 8 * math.sin(x) + 7 * x + 5

n = int(input())
f = list(map(float, input().split()))
l = -1e9
r = 1e9
max_value = r

while abs(r - l) > 2:
    xm = (r + l) / 2
    if calc(xm) >= f[-1]:
        r = xm
    else:
        l = xm
    r = round(r)

for x in range(r - 100, r + 100):
    if abs(calc(x) - f[-1]) < 1e-4:
        r = x
        break

print(round(calc(r + 1), 3))
