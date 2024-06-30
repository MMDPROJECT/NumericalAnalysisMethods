import sympy
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)

def compute_derivative(f, x_input, h, method):
    if method == '1':
        return forward_difference(f, x_input, h)
    elif method == '2':
        return backward_difference(f, x_input, h)
    elif method == '3':
        return central_difference(f, x_input, h)
    elif method == '4':
        return second_derivative(f, x_input, h)
    else:
        raise ValueError("Invalid method")
    
def plot_function_and_tangent(f, x_input, derivative, h):
    sns.set(style="darkgrid")
    
    x_vals = np.linspace(x_input - 10, x_input + 10, 400)
    y_vals = f(x_vals)
    
    tangent_line = derivative * (x_vals - x_input) + f(x_input)
    
    plt.figure(figsize=(10, 6))
    
    sns.lineplot(x=x_vals, y=y_vals, label='Function', linewidth=2.5)
    sns.lineplot(x=x_vals, y=tangent_line, label='Tangent Line', linestyle='--', linewidth=2.5)
    plt.scatter([x_input], [f(x_input)], color='red', zorder=5)
    
    plt.title('Function and Tangent Line', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('f(x)', fontsize=14)
    plt.legend(fontsize=12)
    plt.show()
    
    
    
def main_derivative_taylor():
    x, e = sympy.symbols('x, e')
    
    f = sympy.lambdify(x, sympy.sympify(input("Enter the function in terms of x: ")).subs(e, "exp"), 'numpy') # input function of variable x
    
    while True:
        x_input = float(input('Enter the x that you want to calculate the derivative in: '))
        h = float(input('Enter the h value: '))
        method = input(""" Enter the numerical method that you want to be used in calculating the derivative
        1. Forward Difference
        2. Backward Difference
        3. Central Difference
        4. Second Derivative
        """)
        
        derivative = compute_derivative(f, x_input, h, method)
        print(f"Calculated derivative: {derivative}")
        
        plot_function_and_tangent(f, x_input, derivative, h)
        
        inp = input("Continue?(y/n)")
        if inp == 'n':
            break
    

main_derivative_taylor()