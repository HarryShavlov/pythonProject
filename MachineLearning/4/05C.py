МНК: квадратичная зависимость
  
import numpy as np

with open("input.txt", "r") as f:
    n = int(f.readline())
    data = []
    for _ in range(n):
        x, y = map(float, f.readline().split())
        data.append((x, y))

    X = np.array([[x**2, x, 1] for x, y in data])
    y = np.array([y for x, y in data])

    a, b, c = np.linalg.lstsq(X, y, rcond=None)[0]


with open("output.txt", "w") as f:
    f.write(f"{a:.6f} {b:.6f} {c:.6f}")
