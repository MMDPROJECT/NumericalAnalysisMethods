import numpy as np
import matplotlib.pyplot as plt
import sympy.utilities.lambdify

def get_chebyshew_roots(n: int):
    ks = np.arange(0, n)
    x = np.cos(((2 * ks + 1) * np.pi)/(2 * n))
    return x

def get_divided_difference(f, x: np.ndarray, start, end):
    if start == end: return f(x[start])
    elif end == start + 1: 
        return (f(x[end]) - f(x[start]))/(x[end] - x[start])
    else: 
        return (get_divided_difference(f, x, start + 1, end) - get_divided_difference(f, x, start, end - 1))/(x[end] - x[start])
    
def get_divided_differences(f, x: np.ndarray):
    n = x.size
    divided_differences = np.empty(n, dtype = "float64")
    for i in range(n):
        divided_differences[i] = get_divided_difference(f, x, 0, i)
    return divided_differences

def to_corrected_inval(a: float, b: float, x: float):
    return (2/(b - a))*(x - a) - 1

def P_n(nodes: np.ndarray, divided_differences: np.ndarray, x, a: float, b: float):
    x = to_corrected_inval(a, b, x)
    n = nodes.size
    result = 0
    for i in range(n):
        temp = divided_differences[i]
        for j in range(i):
            temp *= (x - nodes[j])
        result += temp
    return result

# print(to_corrected_inval(-3, 3, 1.5))

# The code works fine in most cases but also would diverge in extreme cases at the end intervals 
# you can see the chebyshew nodes are working efficient if we try to increase n in the interval [-1, 1]
str_of_function = input("Enter the function that you want to interpolate using chebyshew nodes: ")
f = sympy.utilities.lambdify("x", str_of_function, "numpy")
n = int(input("Enter the degree of the polynomial that you want to interpolate the function with: "))
chebyshew_nodes = get_chebyshew_roots(n) # here we calculate the chebyshew nodes for the n-th degree interpolation
divided_differences = get_divided_differences(f, chebyshew_nodes) # here we calculate divided differences using chebyshew nodes
start, end = map(float, input("Enter the start and end intervals that you want to plot the function and it's interpolation: ").split())
xs = np.linspace(start, end, 100) # we divide the interval [-1, 1] into 100 nodes
Y = f(xs) # Real values of the function
Y_hat = P_n(chebyshew_nodes, divided_differences, xs, start, end) # Estimation of the function using interpolation
plt.plot(xs, Y, color = 'red', markersize = "1", linewidth = "2", linestyle = "dashdot", marker = "*", label = "f(x)")
plt.plot(xs, Y_hat, color = "blue", markersize = "0.25", linewidth = "0.5", linestyle = "-", marker = "o", label = "Pn(x)")
plt.legend()
plt.show()
