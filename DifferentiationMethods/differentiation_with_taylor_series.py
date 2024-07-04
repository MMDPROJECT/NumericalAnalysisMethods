import sympy
import matplotlib.pyplot as plt
import numpy as np

def forward_difference(f, x, h):
    """Calculate the forward difference derivative."""
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    """Calculate the backward difference derivative."""
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h):
    """Calculate the central difference derivative."""
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f, x, h):
    """Calculate the second derivative using central difference."""
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)

def compute_derivative(f, x_input, h, method):
    """Compute the derivative using the specified method."""
    difference_formulas = {
        1: forward_difference,
        2: backward_difference,
        3: central_difference,
        4: second_derivative
    }
    if method in difference_formulas.keys():
        return (difference_formulas[method])(f, x_input, h)
    else:
        raise ValueError("Invalid method. Choose 1, 2, 3, or 4.")

def plot_function_and_tangent(f, x_input, derivative, h):
    """Plot the function and its tangent line."""
    x_vals = np.linspace(x_input - 10, x_input + 10, 400)
    y_vals = f(x_vals)
    
    tangent_line = derivative * (x_vals - x_input) + f(x_input)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='Function', linewidth=2.5)
    plt.plot(x_vals, tangent_line, label='Tangent Line', linestyle='--', linewidth=2.5)
    plt.scatter([x_input], [f(x_input)], color='red', zorder=5)
    plt.title('Function and Tangent Line', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.legend(fontsize=12)
    plt.show()

def main_derivative_taylor():
    x, e = sympy.symbols('x, e')
    
    f = sympy.lambdify(x, sympy.sympify(input("Enter the function in terms of x: ")).subs(e, "exp"), 'numpy')
    
    while True:
        x_input = float(input('Enter the x for derivative calculation: '))
        h = float(input('Enter the h value: '))
        method = int(input("""Choose the numerical method for derivative calculation:
        1. Forward Difference
        2. Backward Difference
        3. Central Difference
        4. Second Derivative
        """))
        
        derivative = compute_derivative(f, x_input, h, method)
        print(f"Calculated derivative: {derivative}")

        if 1 <= method <= 3:
            plot_function_and_tangent(f, x_input, derivative, h)
        
        inp = input("Continue? (y/n): ")
        if inp.lower() == 'n':
            break

main_derivative_taylor()