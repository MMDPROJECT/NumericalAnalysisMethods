import numpy as np
import matplotlib.pyplot as plt
import sympy

# Define symbols for mathematical operations
x, t, e = sympy.symbols('x t e')

def get_chebyshew_roots(n: int):
    """
    Generate Chebyshev nodes.
    
    Parameters:
    - n: Degree of the polynomial plus one.
    
    Returns:
    An array of Chebyshev nodes.
    """
    n += 1
    return np.cos(((2 * np.arange(0, n)) * np.pi) / (2 * n))

def get_divided_difference(f_t, nodes: np.ndarray, start, end):
    """
    Compute the divided difference of order k for a given set of nodes.
    
    Parameters:
    - f_t: Function to interpolate in terms of t.
    - nodes: Array of nodes.
    - start, end: Indices defining the interval for the divided difference calculation.
    
    Returns:
    The divided difference of order k.
    """
    if start == end:
        return f_t(nodes[start])
    elif end == start + 1:
        return (f_t(nodes[end]) - f_t(nodes[start])) / (nodes[end] - nodes[start])
    else:
        return (get_divided_difference(f_t, nodes, start + 1, end) - get_divided_difference(f_t, nodes, start, end - 1)) / (nodes[end] - nodes[start])

def get_divided_differences(f_t, nodes: np.ndarray):
    """
    Compute all divided differences for a given set of nodes.
    
    Parameters:
    - f_t: Function to interpolate in terms of t.
    - nodes: Array of nodes.
    
    Returns:
    An array of divided differences.
    """
    n = nodes.size
    divided_differences = np.empty(n, dtype="float")
    for i in range(n):
        divided_differences[i] = get_divided_difference(f_t, nodes, 0, i)
    return divided_differences

def normalize_to_t(a: float, b: float, x: float):
    """
    Normalize a value x to the normalized domain [-1, 1].
    
    Parameters:
    - a, b: Domain bounds.
    - x: Value to normalize.
    
    Returns:
    Normalized value.
    """
    return (2 * (x - a) / (b - a)) - 1

def denormalize_to_x(a: float, b: float, t):
    """
    Denormalize a value t from the normalized domain [-1, 1] to the original domain [a, b].
    
    Parameters:
    - a, b: Domain bounds.
    - t: Normalized value.
    
    Returns:
    Denormalized value.
    """
    return ((t + 1) * (b - a)) / 2 + a

def get_t_of_x(a: float, b: float, x: sympy.Symbol):
    """
    Convert x to t in the normalized domain [-1, 1].
    
    Parameters:
    - a, b: Domain bounds.
    - x: Symbolic x.
    
    Returns:
    Expression converting x to t.
    """
    return sympy.sympify("(2/(b - a))*(x - a) - 1")

def get_x_of_t(a: float, b: float, t: sympy.Symbol):
    """
    Convert t in the normalized domain [-1, 1] back to x in the original domain [a, b].
    
    Parameters:
    - a, b: Domain bounds.
    - t: Symbolic t.
    
    Returns:
    Expression converting t back to x.
    """
    return sympy.sympify("((t + 1)*(b - a)/2) + a")

def P_n_of_t(f_t_sym, nodes: np.ndarray, x: sympy.Symbol, t: sympy.Symbol, a: float, b: float):
    """
    Compute the interpolating polynomial in terms of t.
    
    Parameters:
    - f_t_sym: Symbolic expression of the function in terms of t.
    - nodes: Array of Chebyshev nodes.
    - x, t: Symbols.
    - a, b: Domain bounds.
    
    Returns:
    Interpolating polynomial in terms of t.
    """
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
    """
    Main function to perform Chebyshev interpolation and plotting.
    """
    # Input handling
    f_x_sym = sympy.sympify(input("Enter the function that you want to interpolate using Chebyshev nodes: "))
    n = int(input("Enter the degree of the polynomial that you want to interpolate the function with: "))
    a, b = map(float, input("Enter the start and end intervals that you want to plot the function and its interpolation: ").split())
    
    # Conversion functions
    x_of_t = get_x_of_t(a, b, t)
    t_of_x = get_t_of_x(a, b, x)
    f_t_sym = f_x_sym.subs(x, x_of_t)
    
    # Evaluation and plotting
    chebyshew_nodes = get_chebyshew_roots(n)
    p_n_of_t_sym = P_n_of_t(f_t_sym, chebyshew_nodes, x, t, a, b)
    p_n_of_t = sympy.utilities.lambdify('t', p_n_of_t_sym, "numpy")
    p_n_of_x_sym = p_n_of_t_sym.subs(t, t_of_x)
    p_n_of_x = sympy.utilities.lambdify('x', p_n_of_x_sym, "numpy")
    
    # Plotting
    xs = np.linspace(a, b, 100)
    Y = f_x_sym.subs(x, xs)
    Y_hat = p_n_of_x(xs)
    
    plt.figure(figsize=(8, 6))
    plt.plot(xs, Y, color='red', markersize=1, linewidth=3, linestyle='dashdot', marker='*', label=f"f(x) = {str(f_x_sym)}")
    plt.plot(xs, Y_hat, color='blue', markersize=0.25, linewidth=1, linestyle='-', marker='o', label=f'Pn(x)')
    plt.title("Function Approximation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

chebyshew_main()
