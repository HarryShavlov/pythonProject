Марковские коты

import numpy as np

class CatPopulation:
    def __init__(self, N: int, T: int, probabilities: np.ndarray, counts: np.ndarray, initial_population: np.ndarray):
        self.N = N
        self.T = T
        self.probabilities = probabilities
        self.counts = counts
        self.population = initial_population

    def simulate(self):
        for _ in range(self.T):
            next_population = np.dot(self.population, self.probabilities * self.counts)
            self.population = next_population
        return self.population


N, T = map(int, input().split())
probabilities = np.array([list(map(float, input().split())) for _ in range(N)])
counts = np.array([list(map(int, input().split())) for _ in range(N)])
initial_population = np.array(list(map(int, input().split())))

population = CatPopulation(N, T,probabilities,counts, initial_population)

result = population.simulate()
print(' '.join(map(str, result)))
