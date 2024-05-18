import numpy as np
import matplotlib.pyplot as plt
from sympy import *

x = []
y = []

#Convert (x,y) to their determination list
while true:
    data = input("Add point like this format (x,y): ")
    data = data.strip("()").replace(" ", "")
    point = list(map(int, data.split(",")))
    continue_point = input("Do you still want to add points? (y/n) ")
    x.append(point[0])
    y.append(point[1])
    if continue_point == "n":
        break

n = int(input("Enter the degree n (for Pn(x)):: "))
px = float(input("Enter the x-value at which to find the interpolation:: "))

choosen_x = symbols("x")
# Total Formulation
def f(i):
    return y[i]


def L(i, x):
    mult = 1
    for j in range(len(x)):
        if i != j:
            mult *= (choosen_x - x[j]) / (x[i] - x[j])
    return mult


def pn(x, f, n):
    sums = 0
    for i in range(n + 1):
        sums += f(i) * L(i, x)
    return sums


print("p(" + str(n) + ") :: " + str(pn(x, f, n)))

# PLOT
p = pn(x, f, n)
x_range = np.linspace(min(x), max(x), 100)
y_range = [p.subs(choosen_x, x_val) for x_val in x_range]

plt.figure(figsize=(12, 6))
plt.plot(x_range, y_range)
plt.scatter([px], [p.subs(choosen_x, px)], color="g", marker="o")
plt.title(f"P({n})")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
