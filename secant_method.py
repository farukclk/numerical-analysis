#!/bin/python3
"""

Newton-Raphson Formula:

x1 = x0 - f(x0) / f'(x0)
x2 = x1 - f(x1) / f'(x1)


            f(x0) - f(x1)  
f'(x1) =   ---------------
            ( x0) - x1) )

            
General Secant Method Formula:

                          (x0 - x1)
x2 = x1  -  f(x1)  *   ----------------
                        f(x0) - f(x1)

"""

import math


def f(x):
    e = math.e
    return e**(-2*x) -x - math.sin(x) + 2



def secant_method(x0 , x1):  # x(-1) , x(0)
    iteration = 0
    
    while True:
        iteration += 1
        x = x1 - f(x1) * (x0 - x1) / (f(x0) - f(x1))

        if (iteration != 1 and result == f(x)): # stop condition
            result = f(x)
            print(f"{str(iteration).zfill(2)}. iteration:    " + f" f(x) = {result}".ljust(35) + f" x = {str(x)}")
            break
        
        
        result = f(x)

        x0, x1 = x1, x

        print(f"{str(iteration).zfill(2)}. iteration:    " + f" f(x) = {result}".ljust(35) + f" x = {str(x)}")
    
    return x

     
     


if __name__ == "__main__":	
	print("x:", secant_method(0.5, 1))
