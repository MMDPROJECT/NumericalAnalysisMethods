# Bisection Method

import numpy as np

# for example function f(x) is given
# def f(x):
#     return np.cos(x)


def string_to_function(expression):
    def function(x):
        return eval(expression)
    return function

# we start off by finding a root interval; It will return a single number if it has already found the root or return a tuple consisting (a, b)
# def root_interval_finder(f):
#     a, b = 1, 2
#     f_a, f_b = f(a), f(b)

#     while True:
#         if f_a == 0: return a
#         elif f_b == 0: return b
#         elif f_a * f_b < 0: return (a, b)
#         else: 
#             a -= 10
#             b += 10


# then we start by diving the length of the interval to get to the root
# f: function that we want to find the root of, a: start of the interval, b: end of the interval, e: maximum desired error, d: number of digits that we are allowed to store after decimal point, i: maximum number of iteration desired, which is 20 by default
def bisection_method(f, a, b, e, d, i = 20):
    a, b = round(a, d), round(b, d)
    iterations = (
        list()
    )  
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
