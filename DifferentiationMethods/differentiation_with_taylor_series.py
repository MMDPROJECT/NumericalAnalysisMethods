import sympy

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)

x, e = sympy.symbols('x, e')

f = sympy.lambdify(x, sympy.sympify(input("Enter the function in terms of x ")).subs(e, "exp"), 'numpy') # input function of variable x

while True:
    x_input = float(input('Enter the x that you want to calculate the derivative in: '))
    h = float(input('Enter the h value: '))
    method = input(""" Enter the numerical method that you want to be used in calculating the derivative
    1. Forward Difference
    2. Backward Difference
    3. Central Difference
    4. Second Derivative
    """)
    match method:
        case '1':
            print(forward_difference(f, x_input, h))

        case '2':
            print(backward_difference(f, x_input, h))

        case '3':
            print(central_difference(f, x_input, h))

        case '4':
            print(second_derivative(f, x_input, h))

        case _:
            pass
    inp = input("Continue?(y/n)")
    if inp == 'n':
        break
    

