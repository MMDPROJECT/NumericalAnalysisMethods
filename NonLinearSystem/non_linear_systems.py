import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import seaborn as sns
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def plot_functions_and_points(f, g, history):
    sns.set(style="whitegrid")
    
    # Define the grid for plotting
    x_vals = np.linspace(-10, 10, 400)
    y_vals = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    x_sym, y_sym = sp.symbols('x y')
    f_func = sp.lambdify((x_sym, y_sym), f, 'numpy')
    g_func = sp.lambdify((x_sym, y_sym), g, 'numpy')

    Z_f = f_func(X, Y)
    Z_g = g_func(X, Y)

    plt.figure(figsize=(12, 8))

    # Plot the contours of f and g
    contour_f = plt.contour(X, Y, Z_f, levels=[0], colors='blue', linewidths=2.0)
    contour_g = plt.contour(X, Y, Z_g, levels=[0], colors='red', linewidths=2.0)
    
    # Adding labels to contours
    plt.clabel(contour_f, inline=1, fontsize=10, fmt="f(x,y)")
    plt.clabel(contour_g, inline=1, fontsize=10, fmt="g(x,y)")

    # Plot the history points
    history = np.array(history)
    plt.plot(history[:, 0], history[:, 1], 'ko--', label='Newton-Raphson Path', markersize=5)
    plt.scatter(history[:-1, 0], history[:-1, 1], c='black', s=50, zorder=5)
    plt.scatter(history[-1, 0], history[-1, 1], c='red', s=50, zorder=5, label='Final Point')

    # Additional plot settings
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Newton-Raphson Iterations on Nonlinear System', fontsize=16)
    plt.legend()
    plt.grid(True)
    sns.despine()

    # Zoomed-in inset plot
    ax_inset = inset_axes(plt.gca(), width="30%", height="30%", loc="upper left", borderpad=2.5)
    ax_inset.contour(X, Y, Z_f, levels=[0], colors='blue', linewidths=2.0)
    ax_inset.contour(X, Y, Z_g, levels=[0], colors='red', linewidths=2.0)
    ax_inset.plot(history[:, 0], history[:, 1], 'ko--', markersize=5)
    ax_inset.scatter(history[:-1, 0], history[:-1, 1], c='black', s=50, zorder=5)
    ax_inset.scatter(history[-1, 0], history[-1, 1], c='red', s=50, zorder=5)
    ax_inset.set_xlim(min(history[:, 0])-1, max(history[:, 0])+1)
    ax_inset.set_ylim(min(history[:, 1])-1, max(history[:, 1])+1)
    ax_inset.set_title('Zoomed-in view')

    plt.show()
    
    
def main_non_linear():
    # Step 1: Get the function string from the user
    func_str1 = input("Enter the first function of two variables (e.g., 'x**2 + y**2'): ")
    func_str2 = input("Enter the second function of two variables (e.g., 'x**2 + y**2'): ")

    # Step 2: Parse the string to create a SymPy expression
    x_sym, y_sym = sp.symbols('x y')  # Define the variables
    f = sp.sympify(func_str1)  # Convert the string to a SymPy expression
    g = sp.sympify(func_str2)

    # Step 3: Use lambdify to create a numerical function
    M = sp.Matrix([f, g])
    M_func = sp.lambdify((x_sym, y_sym), M, 'numpy')
    
    # Step 4: Compute the Jacobian matrix and its numerical function
    J = sp.Matrix([[sp.diff(f, x_sym), sp.diff(f, y_sym)], 
                   [sp.diff(g, x_sym), sp.diff(g, y_sym)]])
    J_func = sp.lambdify((x_sym, y_sym), J, 'numpy')
    
    
    x0, y0 = map(float, input("Enter the starting point (x0, y0) separated by a space: ").split())
    
    # Step 6: Implement the Newton-Raphson update step
    history = []
    tol = 1e-6  # Convergence tolerance
    max_iter = 1000  # Maximum number of iterations

    for i in range(max_iter):
        history.append((x0, y0))
        J_inv = np.linalg.inv(J_func(x0, y0))
        F_val = np.array(M_func(x0, y0)).astype(float).flatten()
        delta = J_inv @ F_val

        x_new, y_new = np.array([x0, y0]) - delta

        # Check for convergence
        if np.linalg.norm(delta, ord=2) < tol:
            break
        
        x0, y0 = x_new, y_new
    else:
        raise ValueError("Newton-Raphson did not converge within the maximum number of iterations")

    print(f"Solution: x = {x0}, y = {y0}")
    print("History of iterations:")
    for idx, (x_hist, y_hist) in enumerate(history):
        print(f"Iteration {idx}: x = {x_hist}, y = {y_hist}")  
        
    # Step 7: Plotting
    plot_functions_and_points(f, g, history)
    
if __name__ == '__main__':
    main_non_linear()
# x**2 + y**2 - 4
# x**2 - y**2 - 1
# 1 1