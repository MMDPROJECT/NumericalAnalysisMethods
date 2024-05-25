import numpy as np
import matplotlib.pyplot as plt
import sympy.utilities.lambdify
    
def get_divided_difference(points, start_index, end_index):
    if start_index == end_index: return points[start_index][1]
    elif end_index == start_index + 1: 
        return (points[end_index][1] - points[start_index][1])/(points[end_index][0] - points[start_index][0])
    else: 
        return (get_divided_difference(points, start_index + 1, end_index) - get_divided_difference(points, start_index, end_index - 1))/(points[end_index][0] - points[start_index][0])
    
def interpolation_with_points():    
    # Reading the interpolation points
    n = 0
    points = []
    while(1):
        point = input(f"x{n} f(x{n}): ")
        if point != "":
            point = list(map(float, point.split()))
            points.append(point)
        else:
            break
        n += 1

    # finding the interpolation funciton
    x = sympy.Symbol('x')
    interpolation_function = 0
    for i in range(n):
        divided_difference = get_divided_difference(points, 0, i)
        pi = 1
        for j in range(i):
            pi *= (x - points[j][0])
        term = divided_difference * pi
        interpolation_function += term

    print(interpolation_function)

    f = sympy.utilities.lambdify("x", str(interpolation_function), "numpy")

    # plotting points
    fig = plt.subplot()
    fig.scatter([i[0] for i in points], [i[1] for i in points])

    # plotting function
    lower_bound = min(points, key=lambda x: x[0])[0]
    upper_bound = max(points, key=lambda x: x[0])[0]
    x_test_points = np.linspace(lower_bound - 1, upper_bound + 1)
    y_test_points = [f(i) for i in x_test_points] 
    fig.plot(x_test_points, y_test_points)
    plt.show()
    
def interpolation_with_fx(): 
    # reading the f(x)
    f = input("f(x) = ")
    f = sympy.utilities.lambdify("x", str(f), "numpy")
    
    # Reading the interpolation points
    n = 0
    points = []
    while(1):
        point = input(f"x{n}: ")
        if point != "":
            point = float(point)
            points.append([point, f(point)])
        else:
            break
        n += 1

    # finding the interpolation funciton
    x = sympy.Symbol('x')
    interpolation_function = 0
    for i in range(n):
        divided_difference = get_divided_difference(points, 0, i)
        pi = 1
        for j in range(i):
            pi *= (x - points[j][0])
        term = divided_difference * pi
        interpolation_function += term

    simplified = sympy.simplify(interpolation_function)
    print(simplified)

    interpolation_function = sympy.utilities.lambdify("x", str(interpolation_function), "numpy")

    # plotting points
    fig = plt.subplot()
    fig.scatter([i[0] for i in points], [i[1] for i in points])

    # plotting function
    lower_bound = min(points, key=lambda x: x[0])[0]
    upper_bound = max(points, key=lambda x: x[0])[0]
    x_test_points = np.linspace(lower_bound - 1, upper_bound + 1)
    y_test_points = [interpolation_function(i) for i in x_test_points] 
    y_actual_points = [f(i) for i in x_test_points] 
    fig.plot(x_test_points, y_test_points)
    fig.plot(x_test_points, y_actual_points)
    plt.show()

def newton_main():
    print("1. Enter f(x) with points")
    print("2. Enter interpolation points in this format: (xi, f(xi))")
    print("=> ", end='')
    
    command = input()
    
    if command == "1":
        interpolation_with_fx()
    else:
        interpolation_with_points()


if __name__ == '__main__':
    newton_main()
