Требуется реализовать на языке Python класс stack_chain. У класса должен быть следующий интерфейс:

from __future__ import annotations

from collections.abc import Iterable, Iterator

class stack_chain:

    def __init__(self, *iterables: Iterable):
        """Iterates over iterables in Last In First Out order.

        Arguments:
            iterables: iterables to iterate over"""
        raise NotImplementedError()

    def __iter__(self) -> Iterator:
        """Returns iterator over stored iterables"""
        raise NotImplementedError()

    def __iadd__(self, iterable: Iterable) -> stack_chain:
        """Add a new iterable on top of stack in-place

        Arguments:
            iterable: iterable to add

        Returns:
            self
        """
        raise NotImplementedError()
Класс должен удовлетворять Iterable. stack_chain итерируется по iterables в порядке «последним пришёл — первым ушёл». Объект должен позволять добавлять новый Iterable на вершину стека с использованием оператора +=.

Возвращаемый итератор должен позволять продолжать итерацию после вызова исключения StopIteration, если в stack_chain был добавлен новый Iterable.

from __future__ import annotations
from collections.abc import Iterable, Iterator

class stack_chain:

    def __init__(self, *iterables: Iterable):
        self.iterables = iterables
        self.iterators = [iter(it) for it in iterables]

    def __iter__(self) -> Iterator:
        return self

    def __next__(self):
        while self.iterators:
            try:
                return next(self.iterators[-1])
            except StopIteration:
                self.iterators.pop()
        raise StopIteration


    def __iadd__(self, iterable: Iterable) -> stack_chain:
        self.iterables += (iterable,)
        self.iterators.append(iter(iterable))
        return self
      
 print(*stack_chain(range(3), range(2, -1, -1), (i * i for i in range(3))))


