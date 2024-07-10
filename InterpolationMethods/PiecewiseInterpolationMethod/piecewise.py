import matplotlib.pyplot as plt
import numpy as np
import sympy

def linear_spline(xp, yp, function='n'):
    """
    Generates a linear spline plot.

    Args:
        xp (list): List of x-coordinates.
        yp (list): List of y-coordinates.
        function (str): Optional real function to overlay (default: 'n').

    Returns:
        None
    """
    if function != 'n':
        func = sympy.utilities.lambdify('x', function, 'numpy')
        x_f = np.arange(xp[0], xp[-1], 0.1)
        y_f = list(func(i) for i in x_f)
        plt.plot(x_f, y_f, color='red', label='Real Function')

    plt.plot(xp, yp, color='blue', label='Linear Spline')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def cube_spline(xp, yp, function='null'):
    """
    Generates a cubic spline plot.

    Args:
        xp (list): List of x-coordinates.
        yp (list): List of y-coordinates.
        function (str): Optional real function to overlay (default: 'null').

    Returns:
        None
    """
    if function != 'n':
        func = sympy.utilities.lambdify('x', function, 'numpy')
        x_f = np.arange(xp[0], xp[-1], 0.1)
        y_f = list(func(i) for i in x_f)
        plt.plot(x_f, y_f, color='red', label='Real Function')

    # Calculate spline coefficients
    fac = []
    for i in range(1, len(xp) - 2):
        a = np.array([[1, xp[i], xp[i - 1] ** 2, xp[i - 1] ** 3],
                      [1, xp[i], xp[i] ** 2, xp[i] ** 3],
                      [1, xp[i + 1], xp[i + 1] ** 2, xp[i + 1] ** 3],
                      [1, xp[i + 2], xp[i + 2] ** 2, xp[i + 2] ** 3]])
        b = np.array([yp[i - 1], yp[i], yp[i + 1], yp[i + 2]])
        fac.append(list(np.linalg.solve(a, b)))

    # Plot spline functions
    for i in range(len(xp) - 1):
        f = sympy.utilities.lambdify('x', f"{fac[i][0]} + ({fac[i][1]})*x + ({fac[i][2]})*x**2 + ({fac[i][3]})*x**3", 'numpy')
        xf = np.arange(xp[i], xp[i + 1], 0.1)
        yf = f(xf)
        plt.plot(xf, yf, color='blue', label='Cube Spline' if i == len(xp) - 2 else None)

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main_piecewise():
    n = int(input('Enter number of points: '))
    print('Enter points:')
    arr = [list(map(float, input().split())) for _ in range(n)]
    deg = int(input("Choose interpolation degree (1 or 3): "))
    fun = input('Enter function (or \"n\" to skip): ')

    arr.sort()
    x = [i[0] for i in arr]
    y = [i[1] for i in arr]

    if deg == 1:
        linear_spline(x, y, fun)
    elif deg == 3:
        cube_spline(x, y, fun)

if __name__ == '__main__':
    main_piecewise()
