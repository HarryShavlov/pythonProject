Требуется реализовать на языке Python функции-декораторы.

Декоратор counter_decorator возвращает функцию, печатающую в консоль количество вызовов Function calls count: 
  {n} и возвращающую результат декорируемой функцию от переданных аргументов.
 
from typing import Callable

def counter_decorator(f: Callable) -> Callable:
    def inner(*a,**kw):
        inner.count+=1
        print(f'Function calls count: {inner.count}')
        return f(*a,**kw)
    inner.count = 0
    return inner
    
def projection_decorator(f: Callable[[int], None]) -> Callable[[int, int, int], None]:
    def inner(x,y,z): 
        f(3*x-7*y+15*z+18)
        return f
    return inner
 
def sum(a: int, b: int):
    print(a + b)

fn = counter_decorator(sum)
fn(1, 2)
fn(4, 5)
fn(-4, 5)

