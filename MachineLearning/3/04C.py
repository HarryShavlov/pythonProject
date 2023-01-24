Требуется реализовать на языке Python класс NesterovAG, который описывает алгоритм ускоренного градиента Нестерова и имеет следующий интерфейс


import numpy as np
class NesterovAG:
    eta: float
    alpha: float

    def __init__(self, *, alpha: float = 0.9, eta: float = 0.1):
        self.eta = eta
        self.alpha = alpha

    def optimize(self, oracle, x0: np.ndarray, *,
             max_iter: int = 100, eps: float = 1e-5) -> np.ndarray:
        x = x0
        v = 0
        for _ in range(max_iter):
            grad = oracle.gradient(x - self.alpha * v)
            if np.linalg.norm(grad) < eps:
                return x
            v = self.alpha * v + self.eta * grad
            x = x - v
        return x
