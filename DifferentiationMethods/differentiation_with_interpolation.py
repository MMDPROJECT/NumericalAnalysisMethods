import sympy
import numpy as np

# Define symbols
x, e, s = sympy.symbols('x, e, s')

def get_nth_delta_of_f(f, i, xs, n):
    """
    Calculates the nth delta of a function recursively.

    Args:
        f (sympy.Function): The function.
        i (int): Current index.
        xs (numpy.ndarray): Array of x-values.
        n (int): Order of the delta.

    Returns:
        float: The nth delta value.
    """
    if n == 0:
        return f(xs[i])
    else:
        return get_nth_delta_of_f(f, i + 1, xs, n - 1) - get_nth_delta_of_f(f, i, xs, n - 1)

def choose_k_of_s(k, s):
    """
    Calculates the binomial coefficient (k choose s).

    Args:
        k (int): Total number of items.
        s (int): Number of items to choose.

    Returns:
        float: The binomial coefficient.
    """
    result = sympy.simplify('1')
    j = sympy.simplify('0')
    while j != k:
        result *= (s - j) / (k - j)
        j += 1
    return result

def get_approximation_expression(f, xs, k, h, n, s):
    """
    Computes the approximation expression for the derivative.

    Args:
        f (function): Input function.
        xs (numpy.ndarray): Array of x-values.
        k (int): Order of derivation.
        h (float): Step size.
        n (int): Number of data points.
        s (sympy.Symbol): Symbol for interpolation.

    Returns:
        sympy.Expr: The approximation expression.
    """
    g = sympy.simplify('0')
    i = 0
    while i + k <= n:
        temp = choose_k_of_s(k + i, s)
        temp = temp.diff(s, k)
        temp *= get_nth_delta_of_f(f, 0, xs, k + i)
        g += temp
        i += 1
    g *= sympy.simplify(1 / (h**k))
    return g

def eval_approximation_expression_at_x(g, h, x0, x_input):
    """
    Evaluates the approximation expression at a specific x-value.

    Args:
        g (sympy.Expr): Approximation expression.
        h (float): Step size.
        x0 (float): Initial x-value.
        x_input (float): Target x-value.

    Returns:
        float: Approximated value.
    """
    s = (x_input - x0) / h
    return g.subs([('s', s)])

def main_derivative_interpolation():
    # Input function
    f_sym = sympy.sympify(input("Enter the function in terms of x: ")).subs(e, "exp")
    f = sympy.lambdify(x, f_sym, 'numpy')

    # Step size and target x-value
    h = float(input('Enter the h value: '))
    x_input = float(input('Enter the x-value for derivative calculation: '))

    # Order of derivation
    k = int(input("Enter the order of derivation (k): "))

    # Generate x-values
    left = np.arange(x_input - 5 * h, x_input, h)
    right = np.arange(x_input, x_input + 5 * h + h, h)
    xs = np.concatenate((left, right))
    n = len(xs) - 1

    # Compute approximation expression
    g = get_approximation_expression(f, xs, k, h, n, s)

    # Evaluate and compare with actual value
    approx_value = eval_approximation_expression_at_x(g, h, xs[0], x_input)
    actual_value = f_sym.diff(x, k).subs(x, x_input)
    print(f"Approximated value: {approx_value}")
    print(f"Actual value: {actual_value}")

if __name__ == '__main__':
    main_derivative_interpolation()
