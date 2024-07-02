import numpy as np
import matplotlib.pyplot as plt
import sympy
import sympy.utilities

def L_i(x, xs, i):
    """
    Calculates the Lagrange basis polynomial Li(x).
    
    Parameters:
    - x: Point at which to evaluate the basis polynomial.
    - xs: Array of x-coordinates of the data points.
    - i: Index of the current basis polynomial.
    
    Returns:
    The value of the Lagrange basis polynomial Li(x).
    """
    n = len(xs)
    product = 1
    for j in range(n):
        if j!= i:
            product *= (x - xs[j]) / (xs[i] - xs[j])
    return product

def P_n(x, xs, ys):
    """
    Evaluates the Lagrange polynomial P_n(x) at a given point x.
    
    Parameters:
    - x: Point at which to evaluate the polynomial.
    - xs: Array of x-coordinates of the data points.
    - ys: Array of y-values corresponding to the data points.
    
    Returns:
    The value of the Lagrange polynomial P_n(x).
    """
    n = len(xs)
    summation = 0
    for i in range(n):
        summation += L_i(x, xs, i) * ys[i]
    return summation

# Initialize empty lists for x and y coordinates of data points
xs = []
ys = []

# Initialize counter for data points
n = 0

# Prompt user for input
f_input = input("Enter the function or press enter if you just want to enter data points: ")

if f_input == "":
    # User enters data points
    while True:
        point = input(f"x{n}: ")
        if not point:
            break
        point = list(map(float, point.split()))
        xs.append(point[0])
        ys.append(point[1])
        n += 1  # Increment counter for data points
        
    # Calculate interpolated values over the sampled x-range
    x_sample = np.linspace(min(xs), max(xs), 100)
    y_sample = P_n(x_sample, xs, ys)
    xs = np.array(xs)
    ys = np.array(ys)
    plt.plot(x_sample, y_sample, label="Interpolation over data points")
else:
    # User defines a function
    f_expression = sympy.utilities.lambdify("x", f_input, "numpy")
    while True:
        point = input(f"x{n}: ")
        if not point:
            break
        point = list(map(float, point.split()))
        xs.append(point[0])
        ys.append(f_expression(point[0]))
        n += 1  # Increment counter for data points
    
    # Calculate interpolated values and plot
    x_sample = np.linspace(min(xs), max(xs), 100)
    y_real = f_expression(x_sample)  # Original function values
    y_sample = P_n(x_sample, xs, ys)
    xs = np.array(xs)
    ys = np.array(ys)
    plt.plot(x_sample, y_sample, label="Interpolation over data points")
    plt.plot(x_sample, y_real, label="Original function")

plt.legend()
plt.show()
