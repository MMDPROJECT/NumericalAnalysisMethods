import numpy as np
from scipy.integrate import romberg
import tkinter as tk
from tkinter import messagebox
import math
import matplotlib.pyplot as plt

def eval_function(expr, x):
    try:
        # Define a safe dictionary with math functions and constants
        safe_dict = {name: getattr(math, name) for name in dir(math) if not name.startswith("__")}
        safe_dict.update({
            'pi': math.pi,
            'e': math.e,
            'x': x,
            'np': np
        })
        return eval(expr, {"__builtins__": None}, safe_dict)
    except Exception as e:
        raise ValueError(f"Error evaluating the function: {e}")

def romberg_rule(f, a, b):
    result = romberg(f, a, b)
    return result

def romberg_rule_gui(f_expr, a, b):
    f = lambda x: eval_function(f_expr, x)
    return romberg_rule(f, a, b)

def calculate_integral():
    try:
        f_expr = function_entry.get().replace("^", "**")  # replace ^ with **
        a = float(a_entry.get())
        b = float(b_entry.get())

        result = romberg_rule_gui(f_expr, a, b)
        result_label.config(text=f"Result: {result:.6f}")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def plot_function(f_expr, a, b, n):
    try:
        f = lambda x: eval_function(f_expr, x)
        x_vals = np.linspace(a, b, 400)
        y_vals = [f(x) for x in x_vals]

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"f(x) = {f_expr}")

        x_trap = np.linspace(a, b, n + 1)
        y_trap = [f(x) for x in x_trap]
        ax.fill_between(x_trap, 0, y_trap, alpha=0.3, label="Romberg Approximation")

        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.set_title("Function Plot and Romberg Approximation")

        plt.show()
    except Exception as e:
        messagebox.showerror("Plotting Error", f"An error occurred while plotting: {e}")
 
def plot_function_gui():
    try:
        f_expr = function_entry.get().replace("^", "**")  # replace ^ with **
        a = float(a_entry.get())
        b = float(b_entry.get())

        plot_function(f_expr, a, b, 30)
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Integration by Romberg Rule")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(7, weight=1)

tk.Label(root, text="Function (in terms of x):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
function_entry = tk.Entry(root)
function_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

tk.Label(root, text="Lower limit (a):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
a_entry = tk.Entry(root)
a_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

tk.Label(root, text="Upper limit (b):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
b_entry = tk.Entry(root)
b_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")


calculate_button = tk.Button(root, text="Calculate", command=calculate_integral)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="we")

plot_button = tk.Button(root, text="Plot", command=plot_function_gui)
plot_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="we")

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=6, column=0, columnspan=2, pady=10, sticky="n")

root.mainloop()
