import numpy as np
from sympy import sympify, symbols

def bisection_method(f, a, b, e=1e-2, d=2, i=20):
    """
    Implements the bisection method to find a root of a function within an interval [a, b].
    
    Parameters:
    - f: Function to find the root of.
    - a, b: Start and end of the interval where the root is sought.
    - e: Maximum desired error.
    - d: Number of digits allowed after the decimal point.
    - i: Maximum number of iterations.
    
    Returns:
    A tuple containing the approximate root and the list of intermediate steps.
    """
    # Round the start and end of the interval to the specified precision.
    a, b = round(a, d), round(b, d)
    
    # Initialize the list to store intermediate steps.
    iterations = []
    
    # Iterate up to the maximum number of times.
    for _ in range(i):
        # Calculate the midpoint of the current interval.
        c = round((a + b) / 2, d)
        
        # Evaluate the function at the start, end, and midpoint of the current interval.
        f_a, f_b, f_c = round(f(a), d), round(f(b), d), round(f(c), d)
        
        # Store the current iteration details.
        iterations.append([a, f_a, b, f_b, c, f_c])
        
        # checking if either a, b or c is the root 
        if f_a == 0:
            return [a, iterations]
        elif f_c == 0:
            return [c, iterations]
        elif f_b == 0:
            return [b, iterations]
        # checking if the error is low
        if abs(f_c) <= e or abs(a - b) <= e:
            return [c, iterations]
        else:
            if f_a * f_c < 0:
                b = c
            else: 
                a = c
    
    # Return the last approximation and the list of iterations if the maximum number of iterations is reached without finding a root.
    return (a + b)/2, iterations