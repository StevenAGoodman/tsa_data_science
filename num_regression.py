import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import sys

# ====================================================================
# This little script expects a tabular csv with two numerical columns:
#     Arg 1: The independent (x) dimesion column name
#     Arg 2: The dependent (y) dimesion column name
# Note! This only handles NUMERIC data, not categorical or other jazz.
# ====================================================================

# Import the csv data
df = pd.read_csv("input.csv")
df.dropna(inplace=True)

# 
x_dim = sys.argv[1]
y_dim = sys.argv[2]
assert x_dim in list(df.columns) and y_dim in list(df.columns), "not valid col names"
assert df.dtypes[x_dim] in ["int64", "float64"] and df.dtypes[y_dim] in ["int64", "float64"]

df = df[[x_dim, y_dim]].groupby(x_dim).mean()
print(df.head())
x, y = (df.index, list(df[y_dim]))

# inital scatter plot
plt.title("Raw scatter plt")
plt.scatter(x, y)

# trying different types of regression: linear, quad, cubic, quartic, expo, log, sin
line = np.linspace(min(x), max(x), 100)

## linear
plt.figure()
plt.title("Linear regression")
plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
linear = lambda x: m * x + b
plt.plot(line, linear(line), color="red")

## simple polynomials 
for i in range(2, 6):
    plt.figure()
    plt.title(f"{["quadratic", "cubic", "quartic", "quintic", "hexic", "heptic", "octic", "nonic", "decic"][i-2]} regression")
    plt.scatter(x, y)
    poly = np.poly1d(np.polyfit(x, y, i))
    plt.plot(line, poly(line), color="red")

# complex polynomial
plt.figure()
plt.title("complex polynomial regression")
plt.scatter(x, y)
poly = np.poly1d(np.polyfit(x, y, 50))
plt.plot(line, poly(line), color="red")

## exponential
plt.figure()
plt.title("exponential regression")
plt.scatter(x, y)
poly = np.poly1d(np.polyfit(np.log(x), y, 1))
plt.plot(line, poly(line), color="red")

## logistic

## sinusodal
plt.figure()
plt.title("sinusodal regression")
plt.scatter(x, y)
sine = lambda x, a, b, c: a * np.sin(b * (x - c))
popt, pcov = curve_fit(sine, x, y, p0=[1,1,1])
sin_fit = sine(line, popt[0], popt[1], popt[2])
plt.plot(line, sin_fit, color="red")

plt.show()
