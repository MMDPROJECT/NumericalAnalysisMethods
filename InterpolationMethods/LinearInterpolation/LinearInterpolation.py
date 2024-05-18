import matplotlib.pyplot as plt
import numpy as np
import sympy


def linear_interpolation(input_data):
    data = np.array(sorted(input_data))
    x_points = list(i[0] for i in data)
    y_points = list(i[1] for i in data)
    plt.plot(x_points, y_points)
    plt.show()


def linear_interpolation2(input_data, func):
    data = np.array(sorted(input_data))
    x_points = list(i[0] for i in data)
    y_points = list(i[1] for i in data)

    f = sympy.utilities.lambdify('x', func, 'numpy')
    x_f = np.arange(x_points[0], x_points[-1], 0.1)
    y_f = list(f(i) for i in x_f)

    plt.plot(x_points, y_points, x_f, y_f)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['Linear Interpolation', 'Your Function'])
    plt.show()


fu = input('Enter function: ')
n = int(input('Enter point number: '))
print('Enter points:')
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

linear_interpolation2(arr, fu)
