Требуется реализовать на языке Python функцию


import matplotlib.pyplot

def draw(plt: matplotlib.pyplot, x: list) -> None:
    pass

import math

import matplotlib
import matplotlib.pyplot as plt

def draw(plt: matplotlib.pyplot, x: list) -> None:
    plt.plot(x, [xi**3 - 2*xi**2 + 50*math.sin(5*xi) + 3 for xi in x], color='green')
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('$x^3 - 2x^2 + 50 \sin(5x) + 3$')
