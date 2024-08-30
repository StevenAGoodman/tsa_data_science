import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib as plt

df = pd.read_csv('input_csv/input.csv', names=['x', 'y'])

def linear_func(x, m, b):
    return m * x + b

x = df['x'].values
y = df['y'].values

results, _ = curve_fit(linear_func, x, y)

plt.plot(x, y, 'b-', label='data')
plt.plot(np.linspace(1, 10, 100), linear_func(np.linspace(1, 10, 100), results[0], results[1]))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()