Пусть имеется некоторый список строк. Требуется для каждой строки определить индекс предыдущего вхождения этой строки в список.

import sys

_arr = {}

for i, line in enumerate(sys.stdin):
    try:
        print(_arr[line])
    except KeyError:
        print(-1)
    _arr[line] = i
