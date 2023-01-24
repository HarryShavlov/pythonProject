
Требуется реализовать на языке Python класс AdaGrad, который описывает алгоритм адаптивного градиентного спуска и имеет следующий интерфейс



import numpy as np

class AdaGrad:

    eta: float
    epsilon: float

    def __init__(self, *, eta: float = 0.1, epsilon: float = 1e-8):
        self.eta = eta
        self.epsilon = epsilon

    def optimize(self, oracle, x0: np.ndarray, *,
                 max_iter: int = 100, eps: float = 1e-5):
        x = x0
        G = 0
        for _ in range(max_iter):
            grad = oracle.gradient(x)
            if np.linalg.norm(grad) < eps:
                return x
            G += grad ** 2
            x = x - self.eta * grad / (np.sqrt(G) + self.epsilon)
        return x
