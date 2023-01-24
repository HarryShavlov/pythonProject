Требуется реализовать на языке Python класс Adam, который описывает одноименный алгоритм и имеет следующий интерфейс

import numpy as np

class Adam:
    eta: float
    beta1: float
    beta2: float
    epsilon: float

    def __init__(self, *, eta: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-8):
        self.eta = eta
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

    def optimize(self, oracle, x0: np.ndarray, *,
                 max_iter: int = 100, eps: float = 1e-5) -> np.ndarray:
        x = x0
        m = 0
        v = 0
        t = 0
        for _ in range(max_iter):
            grad = oracle.gradient(x)
            if np.linalg.norm(grad) < eps:
                return x
            t += 1
            m = self.beta1 * m + (1 - self.beta1) * grad
            v = self.beta2 * v + (1 - self.beta2) * grad ** 2
            x -= (self.eta / (np.sqrt(v / (1 - self.beta2 ** t)) + self.epsilon)) * (m / (1 - self.beta1 ** t))
        return x
