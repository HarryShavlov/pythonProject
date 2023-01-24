Требуется реализовать класс на языке Python, который соответствует следующему интерфейсу.


class GradientOptimizer:
    def __init__(self, oracle, x0):
        self.oracle = oracle
        self.x0 = x0

    def optimize(self, iterations, eps, alpha):
        pass


В конструктор принимаются два аргумента — оракул, с помощью которого можно получить градиент оптимизируемой функции, а также точку, с которой необходимо начать градиентный спуск.

import numpy as np

class GradientOptimizer:
    def __init__(self, oracle, x0):
        self.oracle = oracle
        self.x0 = x0

    def optimize(self, iterations, eps, alpha):
        x = self.x0
        for i in range(iterations):
            grad = self.oracle.get_grad(x)
            if np.linalg.norm(grad) < eps:
                break
            x -= alpha * grad
        return x
