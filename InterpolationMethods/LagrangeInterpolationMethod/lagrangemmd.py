import numpy as np
import matplotlib.pyplot as plt
import sympy
import sympy.utilities

def L_i(x, xs, i):
    n = len(xs)
    product = 1
    for j in range(n):
        if j != i:
            product *= (x - xs[j])/(xs[i] - xs[j])
    return product

def P_n(x, xs, ys):
    n = len(xs)
    print(n)
    summation = 0
    for i in range(n):
        # print(f"i :" + i)
        summation += L_i(x, xs, i) * ys[i]
    return summation


xs = []
ys = []
x_sample = None
y_sample = None
n = 0

f = input("Enter the function or press enter if you just want to enter data points: ")
if f == "":
    while(1):
        point = input(f"x{n}: ")
        if point != "":
            point = list(map(float, point.split()))
            xs.append(point[0])
            ys.append(point[1])
        else:
            break
        n += 1
       
    x_sample = np.linspace(min(xs), max(xs), 100)
    y_sample = P_n(x_sample, xs, ys)
    xs = np.array(xs)
    ys = np.array(ys)
    plt.plot(x_sample, y_sample, label = "Interpolation over data points")


else:
    f = sympy.utilities.lambdify("x", f, "numpy")   
    while(1):
        point = input(f"x{n}: ")
        if point != "":
            point = list(map(float, point.split()))
            xs.append(point[0])
            ys.append(f(point[0]))
        else:
            break
        n += 1
    x_sample = np.linspace(min(xs), max(xs), 100)
    y_real = f(x_sample)
    y_sample = P_n(x_sample, xs, ys)
    xs = np.array(xs)
    ys = np.array(ys)
    plt.plot(x_sample, y_sample, label = "Interpolation over data points")
    plt.plot(x_sample, y_real, label = "Original function")
    
plt.legend()
plt.show()