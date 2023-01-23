Требуется реализовать на языке программирования Python функцию, вычисляющую ближайшую точку из массива к данной в терминах евклидова расстояния


import numpy as np

def nearest(points: np.ndarray, a: np.ndarray) -> np.ndarray:
    '''Returns the point from `points` nearest to `a` in terms of euclidean distance

    Args:
        points: A 2-dimensional np.ndarray
        a: A 1-dimensional np.ndarray, `a`.shape[0] == `points`.shape[1]

    '''
    pass
При решении задачи необходимо использовать библиотеку numpy.

import numpy as np

def nearest(points: np.ndarray, a: np.ndarray) -> np.ndarray:
    distances = np.linalg.norm(points - a, axis=1)
    nearest_idx = np.argmin(distances)
    return points[nearest_idx]
