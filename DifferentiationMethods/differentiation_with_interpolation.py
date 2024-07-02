import sympy
import numpy as np
x, e, s = sympy.symbols('x, e, s')

def get_nth_delta_of_f(f, i, xs, n):
    if n == 0:
        return f(xs[i])
    else:
        return get_nth_delta_of_f(f, i + 1, xs, n - 1) - get_nth_delta_of_f(f, i, xs, n - 1)
    
def choose_k_of_s(k, s):
    result = sympy.simplify('1')
    j = sympy.simplify('0')
    while j != k:
        result *= (s - j) / (k - j)
        j += 1
    return result

def get_approximation_expression(f, xs, k, h, n, s):
    g = sympy.simplify('0')
    i = 0
    while i + k <= n:
        temp = choose_k_of_s(k + i, s)
        temp = temp.diff(s, k)
        temp *= get_nth_delta_of_f(f, 0, xs, k + i)
        g += temp
        i += 1
    g *= sympy.simplify(1/(h**k))
    return g

def eval_approximation_expression_at_x(g, h, x0, x_input):
    s = (x_input - x0) / h
    return g.subs([('s', s)])

def main_derivative_interpolation():        
    f_sym = sympy.sympify(input("Enter the function in terms of x: ")).subs(e, "exp")

    f = sympy.lambdify(x, f_sym, 'numpy') # input function of variable x

    h = float(input('Enter the h value: '))

    x_input = float(input('Enter the x-value that you want to calculate the derivative in: '))

    k = int(input("Enter k(the order of derivation): "))

    left = np.arange(x_input - 5 * h, x_input, h)
    right = np.arange(x_input, x_input + 5 * h + h, h)

    xs = np.concatenate((left, right))
    n = len(xs) - 1
    g = get_approximation_expression(f, xs, k, h, n, s)
    print(f"approximated value : {eval_approximation_expression_at_x(g, h, xs[0], x_input)}")
    print(f"actual value {f_sym.diff(x, k).subs(x, x_input)}")