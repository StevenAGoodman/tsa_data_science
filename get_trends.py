# Determine the potential "movie success" of a fictitious feature film based on different public metrics, 
# such as, but not limited to box office revenue, date of release, movie genre (selected by the team), movie production budget, and more.

# exploratory data analysis
# measures:  revenue, budget, profits (revenue - budget), popularity why is $ the best measure
# things to group/aggregate by:  date of release, date of release in october, year of release (from date), country
# columns that don't matter
# filter production status
# missing data - filter out no $ 

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
