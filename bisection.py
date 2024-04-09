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

        # checking if c is the root
        if f_c == 0:
            return [c, iterations]
        elif f_a * f_c < 0:
            b = c
        else:
            a = c
        # checking if the error is low
        if f_c <= e or abs(a - b) <= e:
            return [c, iterations]
        
f = lambdify('x', "sin(x)",'numpy') # returns a numpy-ready function
a, b = 0, 2

arr = bisection_method(f, a, b)