Требуется реализовать на языке программирования Python функцию

from collections.abc import Generator, Iterable


def take(iterable: Iterable, *, skip: int = 0, step: int = 1, count: int = None) -> Generator:
    if not isinstance(iterable, Iterable):
        raise TypeError
    if not isinstance(skip, int) or not isinstance(step, int):
        raise TypeError
    if not isinstance(count, (int, type(None))):
        raise TypeError
    if skip < 0 or (count is not None and count < 0):
        raise ValueError
    if step < 1:
        raise ValueError

    for i, item in enumerate(iterable):
        if i < skip:
            continue
        if (i - skip) % step == 0:
            if count is not None:
                count -= 1
                if count < 0:
                    break
            yield item
