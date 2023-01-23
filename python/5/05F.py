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
        self._name = None

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if type(value) != str:
            raise ValueError
        if re.fullmatch(r"^[a-zA-Z]+", value) and isinstance(value, str):
            self._name = value
        else:
            raise ValueError
