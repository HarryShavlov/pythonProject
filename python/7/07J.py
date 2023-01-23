Существует набор линий в двумерном пространстве. В этом же пространстве присутствует точка point. Необходимо найти кратчайшие расстояния до всех линий. Требуется реализовать на языке Python функцию, позволяющую находить расстояния от точки point до всех линий. Результатом выполнения этой функции должен быть массив расстояний. Работа должна быть выполнена с применением numpy для хранения и обработки всех данных.


import numpy as np

def calculate(start_points: np.ndarray, end_points: np.ndarray, point: np.ndarray) -> np.ndarray:
    '''Возвращает одномерный np.ndarray, содержащий расстояния до линий

    Args:
        start_points: двумерный np.ndarray, содержащий координаты первых точек линий
        end_points: двумерный np.ndarray, содержащий координаты вторых точек линий
        p: двумерный np.ndarray, содержайщий координаты точки point.
        
        start_points.shape == end_points.shape

    Returns:
        одномерный np.ndarray, содержащий расстояния от точки point до линий
    '''
    pass
При решении задачи необходимо использовать библиотеку numpy.

import numpy as np

def calculate(start_points: np.ndarray, end_points: np.ndarray, point: np.ndarray) -> np.ndarray:
    line = end_points - start_points
    point_line = point - start_points
    projection_lengths = np.sum(line * point_line, axis=-1) / np.sum(line ** 2, axis=-1)
    projection_points = start_points + projection_lengths[:, np.newaxis] * line
    distances = np.linalg.norm(point - projection_points, axis=-1)
    return np.round(distances, 4)
  
print(*calculate(
        np.array([[1,  2.5]]),
        np.array([[3,  2.5]]),
        np.array([[2, 1]])))
