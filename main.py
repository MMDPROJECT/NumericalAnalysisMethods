from InterpolationMethods.Hermit.hermit import hermit_main
from InterpolationMethods.NewtonsInterpolationMethod.newton import newton_main
from InterpolationMethods.PiecewiseInterpolationMethod.piecewise import main_piecewise
from InterpolationMethods.ChebyshewMethod.chebyshew import chebyshew_main
from InterpolationMethods.LagrangeInterpolationMethod.lagrangemam import main_lagrange

inp = input("Enter the method that you want:\n1-chebyshew\n2-hermit\n3-lagrange\n4-newton\n5-piecewie\n")
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
    