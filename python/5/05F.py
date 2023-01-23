Требуется реализовать на языке Python класс Student со свойством name с геттером и сеттером.


class Student:

    def __init__(self):
        pass

    @property
    def name(self) -> str:
        pass
            
Сеттер свойства name должен позволять присваивать только строки, состоящие из пробелов и букв английского алфавита (в любом регистре), в остальных случаях требуется бросать исключение ValueError.

import re

class Student:
    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) ->None:
        if type(value) != str:
            raise ValueError
        if not re.fullmatch(r"[a-zA-Z ]*", value):
            raise ValueError
        self._name = value
