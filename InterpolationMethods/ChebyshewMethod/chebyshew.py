import numpy as np
import matplotlib.pyplot as plt
import sympy.utilities.lambdify

def get_chebyshew_roots(n: int):
    n = n + 1
    ks = np.arange(0, n)
    x = np.cos(((2 * ks + 1) * np.pi)/(2 * n))
    return x

def get_divided_difference(f, x: np.ndarray, t: np.ndarray, start, end):
    if start == end: return f(x[start])
    elif end == start + 1: 
        return (f(x[end]) - f(x[start]))/(t[end] - t[start])
    else: 
        return (get_divided_difference(f, x, t, start + 1, end) - get_divided_difference(f, x, t, start, end - 1))/(t[end] - t[start])
    
def get_divided_differences(f, t: np.ndarray, start, end):
    n = t.size
    x = denormalize_to_x(start, end, t)
    divided_differences = np.empty(n, dtype = "float64")
    for i in range(n):
        divided_differences[i] = get_divided_difference(f, x, t, 0, i)
    return divided_differences

def normalize_to_t(a: float, b: float, x: float):
    return (2 * (x - a) / (b - a)) - 1

def denormalize_to_x(a: float, b: float, t):
    return ((t + 1) * (b - a)) / 2 + a


def P_n(nodes: np.ndarray, divided_differences: np.ndarray, x, a: float, b: float):
    x = normalize_to_t(a, b, x)
    n = nodes.size
    result = 0
    for i in range(n):
        temp = divided_differences[i]
        for j in range(i):
            temp *= (x - nodes[j])
        result += temp
    return result

# The code is 100% accurate for polynomials 
str_of_function = input("Enter the function that you want to interpolate using chebyshew nodes: ")
f = sympy.utilities.lambdify("x", str_of_function, "numpy")
n = int(input("Enter the degree of the polynomial that you want to interpolate the function with: "))
chebyshew_nodes = get_chebyshew_roots(n) # here we calculate the chebyshew nodes for the n-th degree interpolation
start, end = map(float, input("Enter the start and end intervals that you want to plot the function and it's interpolation: ").split())
inp = input("Is there any specific point that you want to be calculated?")
divided_differences = get_divided_differences(f, chebyshew_nodes, start, end) # here we calculate divided differences using chebyshew nodes and the function f
xs = np.linspace(start, end, 100) # we divide the interval [start, end] into 100 nodes
Y = f(xs) # Real values of the function at the specified points xs
Y_hat = P_n(chebyshew_nodes, divided_differences, xs, start, end) # Estimation of the function using interpolation
if inp != '': 
    global single_x_input
    single_x_input = float(inp)
    print(f"Value of interpolation function at {single_x_input} : {P_n(chebyshew_nodes, divided_differences, single_x_input, start, end)}")
    print(f"Value of original function at {single_x_input} : {f(single_x_input)}")
plt.plot(xs, Y, color = 'red', markersize = "1", linewidth = "2", linestyle = "dashdot", marker = "*", label = "f(x)")
plt.plot(xs, Y_hat, color = "blue", markersize = "0.25", linewidth = "0.5", linestyle = "-", marker = "o", label = "Pn(x)")
plt.legend()
plt.show()
