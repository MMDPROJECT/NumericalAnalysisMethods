import sympy.utilities
from sympy import *
import matplotlib.pyplot as plt
import numpy as np

def main_lagrange():
    x = []
    y = []
    index = 0
    # Convert (x,y) to their determination list
    fx = input("Enter the function or press enter if you just want to enter data points: ")
    if fx == "":
        fx = None
        print()
        print("********************************")
        print("Add point like this format (x,y)")
        print("********************************")
        print()
        while True:
            point = input("(x" + str(index) + ", y" + str(index) + "):: ")
            if not point:
                break
            index += 1
            point = list(map(int, point.split()))
            x.append(point[0])
            y.append(point[1])
    else:
        fx = sympy.utilities.lambdify("x", fx, "numpy")
        while True:
            point = input("x" + str(index) + ":: ")
            if not point:
                break
            index += 1
            point = list(map(float, point.split()))
            x.append(point[0])
            y.append(fx(point[0]))

    print()
    n = int(input("Enter the degree n (for Pn(x)):: "))
    print()
    chosen_x = symbols("x")


    # Total Formulation
    def f(i):
        return y[i]


    def L(i, x):
        mult = 1
        for j in range(len(x)):
            if i != j:
                mult *= (chosen_x - x[j]) / (x[i] - x[j])
        return mult


    def pn(x, f, n):
        sums = 0
        for i in range(n + 1):
            sums += f(i) * L(i, x)
        return sums


    print("*** Pn(x) ***")
    print("p" + str(n) + "(x):: " + str(pn(x, f, n)))
    print()
    px = list(
        map(
            float,
            input(
                "Enter the x-values at which to find the interpolation (x for pn(x)): "
            ).split(),
        )
    )
    # PLOT
    p = pn(x, f, n)
    x_range = np.linspace(min(x), max(x), 100)
    y_range = [float(p.subs(chosen_x, x_val)) for x_val in x_range]

    plt.figure(figsize=(12, 6))
    plt.plot(x_range, y_range, color='blue', markersize=0.25, linewidth=1, linestyle='-', marker='o', label= f'Pn(x)')
    if(fx is not None):
        plt.plot(x_range, [fx(x) for x in x_range], color='red', markersize=1, linewidth=3, label= f"f(x)")
    plt.scatter(
        px, [float(p.subs(chosen_x, px_val)) for px_val in px]
    )
    plt.title(f"P{n}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main_lagrange()