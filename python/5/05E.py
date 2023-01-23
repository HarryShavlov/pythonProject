CardStack 

from __future__ import annotations
from typing import Union, Iterable, List
import random

def combine_lists(_self, _other):
    combined_list = []
    i, j = 0, 0
    while i < len(_self) and j < len(_other):
        combined_list.append(_self[i])
        combined_list.append(_other[j])
        i += 1
        j += 1
    while i < len(_self):
        combined_list.append(_self[i])
        i += 1
    while j < len(_other):
        combined_list.append(_other[j])
        j += 1
    return combined_list

class CardStack:
    values: List[int]

    def __init__(self, val: Union[int, Iterable[int], None] = None):
        self.values = []
        if isinstance(val, int):
            sst = list([random.randint(-100, 100) for x in range(val)])
            self.values = sst
        if isinstance(val, Iterable):
            self.values = list(val)

    def shuffled(self) -> CardStack:
        return CardStack(random.sample(self.values, k=len(self.values)))

    def combine(self, other: CardStack) -> CardStack:
        return CardStack(combine_lists(self.values, other.values))

    def add(self, value: int) -> None:
        """Adds a new value on top of the stack"""
        self.values.append(value)

    def __len__(self) -> int:
        return len(self.values)
