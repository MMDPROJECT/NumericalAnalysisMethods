# Bisection Method

import numpy as np
from sympy import sympify, symbols
from sympy.utilities.lambdify import lambdify

import matplotlib.pyplot as plt

# this function converts a given symbol and a expression defined by that to a function. symbol: is something like 'x' or 'y', expression: any arbitrary mathematical expression related to the single given symbol
def string_to_function(symbol, expression):
    symbol = symbols(symbol)
    func = sympify(expression)
    return func

# then we start by diving the length of the interval to get to the root
# f: function that we want to find the root of, a: start of the interval, b: end of the interval, e: maximum desired error, d: number of digits that we are allowed to store after decimal point, i: maximum number of iteration desired, which is 20 by default
def bisection_method(f, a, b, e = 10**(-2), d = 2, i = 20):
    a, b = round(a, d), round(b, d)
    iterations = list()
    # each element will be [a: start point of the interval, f_a, b: end point of the interval, f_b, c: middle of the interval, f_c, i: which iteration it is]
    iteration_number = 0
    while iteration_number <= i:
        iteration_number+= 1
        c = round((a + b) / 2, d)
        f_a, f_b, f_c = round(f(a), d), round(f(b), d), round(f(c), d)
        
        # storing information
        iterations.append([a, f_a, b, f_b, c, f_c, iteration_number])

        # checking if either a, b or c is the root 
        if f_a == 0:
            return [a, iterations]
        elif f_c == 0:
            return [c, iterations]
        elif f_b == 0:
            return [b, iterations]
        # checking if the error is low
        if f_c <= e or abs(a - b) <= e:
            return [c, iterations]
        else:
            if f_a * f_c < 0:
                b = c
            else: 
                a = c
        
"""
-------------------------------------------------------------------------------------------------
Sample code for how to evaluate the given string and finding it's root using bisection method and then plotting it using matplotlib
"""
        
# f = lambdify('x', "sin(x)",'numpy') # returns a numpy-ready function
# a, b = 1, 100

# arr = bisection_method(f, a, b)
# print(arr)

# # extracting the points obtained by the bisection method
# iteration_points = np.array(arr[1])[:, [0, 2, 4]].reshape(-1)
# x_final = arr[0]

# # generating an array of points around the obtained interval by a small tolerance
# x = np.linspace(min(iteration_points), max(iteration_points), 1000)
# y = f(x)

# # scatter plot
# abc_tuples =  np.array(arr[1])[:, [0, 2, 4]]
# # print(abc_tuples)
# iteration_numbers = np.array(arr[1])[:, 6]
# colors = np.random.rand(len(abc_tuples), 3)

# fig, ax = plt.subplots(figsize=(8, 6))

# for i, abc_tuple in enumerate(abc_tuples):
#     a, b, c = abc_tuple[0], abc_tuple[1], abc_tuple[2]
#     # ax.scatter(a, f(a), c=colors[i])
#     # ax.scatter(b, f(b), c=colors[i])
#     ax.scatter(c, f(c), c=colors[i], label=f'i={i}')

# ax.scatter(x_final, f(x_final), c= 'red', label= f'answer')


# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Plot of f(x)')
# plt.grid(True)
# plt.legend()
# plt.show()

# """"-------------------------------------------------------------------------------------------------"""