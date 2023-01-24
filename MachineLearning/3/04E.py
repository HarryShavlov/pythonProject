Требуется реализовать на языке Python класс RMSProp, который описывает одноименный алгоритм и имеет следующий интерфейс



import numpy as np

class RMSProp:

    eta: float
    gamma: float
    epsilon: float

    def __init__(self, *, eta: float = 0.1, gamma: float = 0.9, epsilon: float = 1e-8):
        self.eta = eta
        self.gamma = gamma
        self.epsilon = epsilon

    def optimize(self, oracle, x0: np.ndarray, *,
             max_iter: int = 100, eps: float = 1e-5) -> np.ndarray:
        x = x0
        G = 0
        for _ in range(max_iter):
            grad = oracle.gradient(x)
            if np.linalg.norm(grad) < eps:
                return x
            G = self.gamma * G + (1 - self.gamma) * grad ** 2
            x -= (self.eta / (np.sqrt(G + self.epsilon))) * grad
        return x
