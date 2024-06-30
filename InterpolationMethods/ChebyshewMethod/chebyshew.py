import numpy as np
import matplotlib.pyplot as plt
import sympy.utilities.lambdify
import sympy

# Symbols
x = sympy.Symbol('x')
t = sympy.Symbol('t')
e = sympy.Symbol('e')

def get_chebyshew_roots(n: int):
    n = n + 1
    ks = np.arange(0, n)
    roots = np.cos(((2 * ks + 1) * np.pi)/(2 * n))
    return roots

def get_divided_difference(f_t, nodes: np.ndarray, start, end):
    if start == end:
        return f_t(nodes[start])
    elif end == start + 1: 
        return (f_t(nodes[end]) - f_t(nodes[start]))/(nodes[end] - nodes[start])
    else: 
        return (get_divided_difference(f_t, nodes, start + 1, end) - get_divided_difference(f_t, nodes, start, end - 1))/(nodes[end] - nodes[start])
    
def get_divided_differences(f_t, nodes: np.ndarray):
    n = nodes.size
    divided_differences = np.empty(n, dtype = "float")
    for i in range(n):
        # print(type(get_divided_difference(f_t, nodes, 0, i)))
        divided_differences[i] = get_divided_difference(f_t, nodes, 0, i)
    return divided_differences

def normalize_to_t(a: float, b: float, x: float):
    return (2 * (x - a) / (b - a)) - 1

def denormalize_to_x(a: float, b: float, t):
    return ((t + 1) * (b - a)) / 2 + a

def get_t_of_x(a: float, b: float, x: sympy.Symbol):
    return sympy.sympify("(2/(b - a))*(x - a) - 1").subs([('a', a), ('b', b), ('x', x)])
    
def get_x_of_t(a: float, b: float, t: sympy.Symbol):
    return sympy.sympify("((t + 1)*(b - a)/2) + a").subs([('a', a), ('b', b), ('t', t)])

def P_n_of_t(f_t_sym, nodes: np.ndarray, x: sympy.Symbol, t: sympy.Symbol, a: float, b: float):
    f_t = sympy.utilities.lambdify('t', f_t_sym, "numpy") 
    n = nodes.size - 1
    p_n = sympy.sympify("0")
    divided_differences = get_divided_differences(f_t, nodes)
    for i in range(n + 1):
        temp = sympy.sympify(str(divided_differences[i]))
        for j in range(i):
            temp *= (t - nodes[j])
        p_n += temp
    return p_n

def chebyshew_main():
    # Taking input
    f_x_sym = sympy.sympify(input("Enter the function that you want to interpolate using chebyshew nodes: ")).subs(e, "exp") # input function of variable x
    n = int(input("Enter the degree of the polynomial that you want to interpolate the function with: ")) # degree of the interpolating polynomial
    a, b = map(float, input("Enter the start and end intervals that you want to plot the function and it's interpolation: ").split()) # start and end intervals that we want to interpolate the functing in
    inp = input("Is there any specific point that you want to be calculated? ")
    # Overhead stuff #
    x_of_t = get_x_of_t(a, b, t)
    t_of_x = get_t_of_x(a, b, x)
    f_t_sym = f_x_sym.subs(x, x_of_t)
    f_x = sympy.utilities.lambdify('x', f_x_sym, "numpy")
    # Evaluating the interpolating function #
    chebyshew_nodes = get_chebyshew_roots(n)
    print(f_t_sym)
    p_n_of_t_sym = P_n_of_t(f_t_sym, chebyshew_nodes, x, t, a, b) # symbolic representation of interpolating polynomial
    p_n_of_t = sympy.utilities.lambdify('t', p_n_of_t_sym, "numpy") # lamda function of p_n_t
    p_n_of_x_sym = p_n_of_t_sym.subs(t, t_of_x)
    p_n_of_x = sympy.utilities.lambdify('x', p_n_of_x_sym, "numpy") # lamda function of p_n_x
    # Plotting functions
    xs = np.linspace(a, b, 100) # we divide the interval [a, b] into 100 nodes
    Y = f_x(xs) # Real values of the function at the specified points xs
    Y_hat = p_n_of_x(xs) # Estimation of the function using interpolation
    if inp != '': 
        global single_x_input
        single_x_input = float(inp)
        print(f"Value of interpolation function at {single_x_input} : {p_n_of_x(single_x_input)}")
        print(f"Value of original function at {single_x_input} : {f_x(single_x_input)}")

    plt.figure(figsize=(8, 6))  # Adjust the figure size if needed
    plt.plot(xs, Y, color='red', markersize=1, linewidth=3, linestyle='dashdot', marker='*', label= f"f(x) = {str(f_x_sym)}")
    plt.plot(xs, Y_hat, color='blue', markersize=0.25, linewidth=1, linestyle='-', marker='o', label= f'Pn(x)')
    # Customize the plot
    plt.title("Function Approximation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()