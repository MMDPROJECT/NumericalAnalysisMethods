import matplotlib.pyplot as plt
import numpy as np
import sympy


def linear_spline(xp, yp, function='n'):
    # add real func if is there any
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
    # add real func if there is any
    if function != 'n':
        func = sympy.utilities.lambdify('x', function, 'numpy')
        x_f = np.arange(xp[0], xp[-1], 0.1)
        y_f = list(func(i) for i in x_f)
        plt.plot(x_f, y_f, color='red', label='Real Function')

    fac = []
    # find a0, b0, c0 and d0
    a = np.array([[1, xp[0], xp[0] ** 2, xp[0] ** 3]
                     , [1, xp[1], xp[1] ** 2, xp[1] ** 3]
                     , [1, xp[2], xp[2] ** 2, xp[2] ** 3]
                     , [0, 0, 1, 3 * xp[0]]])
    b = np.array([yp[0], yp[1], yp[2], 0])
    fac.append(list(np.linalg.solve(a, b)))

    # find factors from 1 to n-2
    for i in range(1, len(xp) - 2):
        a = np.array([[1, xp[i], xp[i - 1] ** 2, xp[i - 1] ** 3]
                         , [1, xp[i], xp[i] ** 2, xp[i] ** 3]
                         , [1, xp[i + 1], xp[i + 1] ** 2, xp[i + 1] ** 3]
                         , [1, xp[i + 2], xp[i + 2] ** 2, xp[i + 2] ** 3]])
        b = np.array([yp[i - 1], yp[i], yp[i + 1], yp[i + 2]])
        fac.append(list(np.linalg.solve(a, b)))

    # find an-1, bn-1, cn-1 and dn-1
    a = np.array([[1, xp[-3], xp[-3] ** 2, xp[-3] ** 3]
                     , [1, xp[-2], xp[-2] ** 2, xp[-2] ** 3]
                     , [1, xp[-1], xp[-1] ** 2, xp[-1] ** 3]
                     , [0, 0, 1, 3 * xp[-1]]])
    b = np.array([yp[0], yp[1], yp[2], 0])
    fac.append(list(np.linalg.solve(a, b)))
    print(fac)

    # add spline functions to plot
    for i in range(len(xp) - 1):
        f = sympy.utilities.lambdify('x', f"{fac[i][0]}+({fac[i][1]})*x+({fac[i][2]})*x**2+({fac[i][3]})*x**3", 'numpy')
        xf = np.arange(xp[i], xp[i + 1], 0.1)
        yf = f(xf)
        if i == len(xp) - 2:
            plt.plot(xf, yf, color='blue', label='Cube Spline')
        else:
            plt.plot(xf, yf, color='blue')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main_piecewise():
    # get inputs
    n = int(input('Enter number of points: '))
    print('Enter points:')
    arr = []
    for _ in range(n):
        x, y = map(float, input().split())
        arr.append([x, y])
    deg = int(input("Choose interpolation degree:(1 or 3)\n"))
    fun = input('Enter function:(you can enter \"n\" for skip) \n')

    # sort input
    arr = sorted(arr)
    x = list(i[0] for i in arr)
    y = list(i[1] for i in arr)

    # add spline func to plot
    if deg == 1:
        linear_spline(x, y, fun)
    elif deg == 3:
        cube_spline(x, y, fun)

# 0 0
# 1 1
# -1 1
# 2 16
# -2 16
# 3 81
# -3 81
# 4 256
# -4 256

