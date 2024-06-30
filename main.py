from InterpolationMethods.Hermit.hermit import hermit_main
from InterpolationMethods.NewtonsInterpolationMethod.newton import newton_main
from InterpolationMethods.PiecewiseInterpolationMethod.piecewise import main_piecewise
from InterpolationMethods.ChebyshewMethod.chebyshew import chebyshew_main
from InterpolationMethods.LagrangeInterpolationMethod.lagrangemam import main_lagrange
# from IntegralMethods.Gaussian_Quadrature import main_gaussian
# from IntegralMethods.Newton_cotes import main_newton_cotes
# from IntegralMethods.Rectangler_method import main_rectangle
# from IntegralMethods.Romberg_rule import main_romberg
from NonLinearSystem.nonLinearSystem import main_non_linear
from DifferentiationMethods.differentiation_with_interpolation import main_derivative_interpolation
from DifferentiationMethods.differentiation_with_taylor_series import main_derivative_taylor

def choose_method_interpolation(inp):
    if inp=='4':
        newton_main()
    elif inp=='2':
        hermit_main()
    elif inp=='5':
        main_piecewise()
    elif inp=='1':
        chebyshew_main()
    elif inp=='3':
        main_lagrange()
        
def choose_method_integral(inp):
    # if inp=='1':
        # main_gaussian()
    # elif inp=='2':
    #     main_newton_cotes()
    # elif inp=='3':
    #     main_rectangle()
    # elif inp=='4':
    #     main_romberg()
    pass

def choose_method_diff(inp):
    if(inp=='1'):
        main_derivative_interpolation()
    elif(inp=='2'):
        main_derivative_taylor()
        
def choose_mode(inp):
    if(inp=='1'):
        choose_method_interpolation(inp = input("Enter the method that you want:\n1-Chebyshew\n2-Hermit\n3-Lagrange\n4-Newton\n5-piecewie\n"))
    elif(inp=='2'):
        choose_method_integral(inp = input("Enter the method that you want:\n1-Gaussian_Quadrature\n2-Newton_cotes\n3-Rectangler_method\n4-Romberg_rule\n"))
    elif(inp=='3'):
        main_non_linear()
    elif(inp=='4'):
        choose_method_diff(inp = input("Enter the method that you want:\n1-diff with interpolation\n2-diff with taylor series\n"))

choose_mode(inp = input("Enter the mode that you want:\n1-Interpolation\n2-Integral\n3-Nonlinear system\n4-Diffrentiation\n"))        


    