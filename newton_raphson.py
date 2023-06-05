#!/bin/python3
"""

Newton-Raphson Formula:

x1 = x0 - f(x0) / f'(x0)

"""


import math

def f(x):
	return (0.5 * math.pi -  math.asin(x) - x*(1- x**2)**0.5) - 1.24
	

# f'(x)
def fd(x):
	return -2* (1-x**2)**0.5



def newton_raphson(a, b, tol):
	if (f(a) * f(b) > 0 ):
		print("aralikta kök yok")
		return -1
	
	x1 = a  				# sonsuz donguye giriyorsa a yerine b den basla
	
	difference = tol + 1 	# donguye girebilmek icin gecici atama
	iteration = 0
	
	while (difference > tol):
		iteration += 1
		x0 = x1;
		
		x1 = x0 - f(x0) / fd(x0)
	
		result = f(x1)
		difference = abs(x0 - x1)

		print(f"{str(iteration).zfill(2)}. iteration values:    " + f"stop_condition = {difference}".ljust(42) + f" F(x1) = {result}".ljust(35) + f"x = {x1}")
		
			
	return x1




if __name__ == "__main__":	
	print(newton_raphson(0.1, 0.9, 10**-6))

