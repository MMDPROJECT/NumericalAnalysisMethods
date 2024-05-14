import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# choosen_x = int(input("choose your desire point ::"))
x = list(map(int, input("List :: ").split()))
n = int(input("n :: "))
fx = input("Add function :: ")
px = float(input("Add px :: "))
choosen_x = symbols("x")


# Total Formulation
def f(xi):
    if fx == '':
        return 2 * (xi) ** 2 + 4
    else:
        return sympify(fx).subs(symbols('x'), xi)


def L(i, x):
    mult = 1
    for j in range(len(x)):
        if i != j:
            mult *= (choosen_x - x[j]) / (x[i] - x[j])
    return mult


def pn(x, f, n):
    sums = 0
    for i in range(n + 1):
        sums += f(x[i]) * L(i, x)
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
