Линейная регрессия. Основы

import numpy as np

def linear_func(theta, x):
    return np.dot(theta, x)

def linear_func_all(theta, X):
    return np.dot(X, theta)

def mean_squared_error(theta, X, y):
    return np.mean((y - linear_func_all(theta, X)) ** 2)

def grad_mean_squared_error(theta, X, y):
    m = len(y)
    return -2/m * np.dot(X.T, y - linear_func_all(theta, X))
