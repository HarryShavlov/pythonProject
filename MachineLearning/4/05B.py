Требуется реализовать функцию на языке Python, которая находит линейную регрессию заданных векторов, используя метрику MSE.

def fit_linear_regression(X, y)   # np.array of linear regression coefs
X — двумерный np.array. Каждая строка соответствует отдельному примеру.
y — реальные значения предсказываемой величины


import numpy as np

def fit_linear_regression(X, y):
    X_T = X.T
    coefs = np.linalg.solve(X_T @ X, X_T @ y)
    np.delete(X, 0, axis=0)
    np.delete(y, 0)
    return coefs
