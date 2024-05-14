import numpy as np
import matplotlib.pyplot as plt
import sympy.utilities.lambdify
from math import factorial
diffs ={}

def get_divided_difference(points, start_index, end_index):
    if start_index == end_index: return (points[start_index][1],0)
    elif end_index == start_index + 1: 
        try:
            return ((points[end_index][1] - points[start_index][1])/(points[end_index][0] - points[start_index][0]),0)
        except ZeroDivisionError:
            return (diffs[(points[start_index][0],1)],1)
    else:
        try: 
            first,degree1 = get_divided_difference(points, start_index + 1, end_index)
            second,degree2 = get_divided_difference(points, start_index, end_index - 1)
            return (( first-second )/(points[end_index][0] - points[start_index][0]),0)
        except ZeroDivisionError:
            return (diffs[(points[start_index][0],degree1+1)]/factorial(degree1+1),degree1+1)

# Reading the interpolation points
n = 0
points = []
while(1):
    point = input(f"x{n} + degree diff: ")
    if point != "":
        point = list(map(float, point.split()))
        if point[2]!=0:
            points.append([point[0],diffs[(point[0],0)]])
        else:
            points.append(point[:2])
        diffs[(point[0],point[2])]=point[1]
    else:
        break
    n += 1

# finding the interpolation funciton
x = sympy.Symbol('x')
interpolation_function = 0
for i in range(n):
    divided_difference = get_divided_difference(points, 0, i)[0]
    pi = 1
    for j in range(i):
        pi *= (x - points[j][0])
    term = divided_difference * pi
    interpolation_function += term

print(interpolation_function)

f = sympy.utilities.lambdify("x", str(interpolation_function), "numpy")

str_of_function = input("Enter the function that you want to interpolate using hermit nodes: ")
g = sympy.utilities.lambdify("x", str_of_function, "numpy")

# plotting points
fig = plt.subplot()
fig.scatter([i[0] for i in points], [i[1] for i in points])

# plotting function
lower_bound = min(points, key=lambda x: x[0])[0]
upper_bound = max(points, key=lambda x: x[0])[0]
x_test_points = np.linspace(lower_bound - 1, upper_bound + 1,500)
y_test_points = [f(i) for i in x_test_points]
y_test_original = [g(i) for i in x_test_points] 
fig.plot(x_test_points, y_test_points)
fig.plot(x_test_points, y_test_original)
plt.show()
