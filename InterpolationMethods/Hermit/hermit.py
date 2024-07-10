import numpy as np
import matplotlib.pyplot as plt
import sympy
from math import factorial

def get_divided_difference(points, start_index, end_index, diffs):
    """
    Computes the divided difference of order k for a given set of points.
    
    Parameters:
    - points: List of tuples, where each tuple contains a point's x-coordinate and its corresponding y-value.
    - start_index, end_index: Indices defining the interval for the divided difference calculation.
    - diffs: Dictionary storing previously computed divided differences.
    
    Returns:
    A tuple containing the divided difference and its degree.
    """
    if start_index == end_index:
        return points[start_index][1], 0
    elif end_index == start_index + 1:
        try:
            return ((points[end_index][1] - points[start_index][1]) / (points[end_index][0] - points[start_index][0]), 0)
        except ZeroDivisionError:
            return diffs.get((points[start_index][0], 1), 0), 1
    else:
        try:
            first, degree1 = get_divided_difference(points, start_index + 1, end_index, diffs)
            second, degree2 = get_divided_difference(points, start_index, end_index - 1, diffs)
            return ((first - second) / (points[end_index][0] - points[start_index][0]), 0)
        except ZeroDivisionError:
            key = (points[start_index][0], degree1 + 1)
            if key not in diffs:
                diffs[key] = 0
            return diffs[key] / factorial(degree1 + 1), degree1 + 1

def hermit_main():
    """
    Main function to perform Hermit interpolation and plotting.
    """
    # Reading the original function from user
    str_of_function = input("Enter the function that you want to interpolate using Hermit nodes: ")
    g = sympy.utilities.lambdify("x", str_of_function, "numpy")
    
    # Reading the interpolation points
    points = []
    diffs = {}
    n = 0  # Variable 'n' to track the number of points
    while True:
        point = input(f"x{n} + degree differentiation: ")
        if not point:
            break
        point = list(map(float, point.split()))
        if point[2]!= 0:
            points.append([point[0], diffs.get((point[0], 0), 0)])
        else:
            points.append(point[:2])
        diffs[(point[0], point[2])] = point[1]
        n += 1  # Increment 'n' each time a new point is added
    
    # Finding the interpolation function
    x = sympy.Symbol('x')
    interpolation_function = sum(
        (get_divided_difference(points, 0, i, diffs)[0] * sympy.factorial(i) * sympy.prod(x - point[0] for point in points[:i])) for i in range(len(points))
    )
    print(interpolation_function)
    f = sympy.utilities.lambdify("x", str(interpolation_function), "numpy")
    
    # Plotting points and function
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Ensure points is structured correctly before attempting to unzip
    if len(points) > 0:
        x_coords, y_coords = zip(*points)
        ax.scatter(x_coords, y_coords, color='red')  # Scatter plot for interpolation points
    else:
        print("No points were entered.")
        return  # Exit the function early if no points were entered

    lower_bound, upper_bound = min(x_coords), max(x_coords)
    x_test_points = np.linspace(lower_bound - 1, upper_bound + 1, 500)
    y_test_points = [f(i) for i in x_test_points]
    y_test_original = [g(i) for i in x_test_points]

    ax.plot(x_test_points, y_test_points, label='Interpolation')  # Plot interpolated function
    ax.plot(x_test_points, y_test_original, '--', label='Original Function')  # Plot original function
    ax.set_title("Hermit Interpolation")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    plt.show()


    # Interpolate a specific point
    while True:
        point = input("Enter the number that you want to interpolate: ")
        if not point:
            break
        point = list(map(float, point.split()))
        print(f"Interpolation of the point {point[0]}: {f(point[0])}")

if __name__ == '__main__':
    hermit_main()