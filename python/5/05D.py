Требуется реализовать на языке Python класс ShiftableList(list), который наследуется от list и реализует операторы циклического сдвига влево (<<) и вправо (>>). 
Результатом выполнения этих операций должен быть новый объект, при этом исходный не изменяется. 
Если операнд справа от оператора сдвига имеет тип, отличный от int, необходимо вызвать исключение TypeError. 
В случае, если величина сдвига отрицательна, должен выполниться сдвиг в противоположную сторону на количество позиций, равное модулю этой величины.

class ShiftableList(list):
    def __lshift__(self, shift):
        st = abs(shift) % len(self)
        if shift <0:
            return ShiftableList(self[-st:] + self[:-st])
        else:
            return ShiftableList(self[st:] + self[:st])

    def __rshift__(self, shift):
        if not isinstance(shift, int):
            raise TypeError("оператор сдвига имеет тип, отличный от int")
        st = abs(shift) % len(self)
        if shift < 0:
            return ShiftableList(self[st:] + self[:st])
        else:
            return ShiftableList(self[-st:] + self[:-st])
          
lst = ShiftableList(['a', 'b', 'c'])
lst2 = lst << 1 
print(', '.join(lst2))
