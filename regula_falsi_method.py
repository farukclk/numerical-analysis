#!/bin/python3

import math

def f(x):
	return math.acos(x) - x
	

	
# regula_falsi
def regula_falsi(a, b, tol):
	if (f(a) * f(b) > 0 ):
		print("aralikta kök yok")
		return -1
	
	stop_condition = tol + 1  # donguye girebilmek icin
	iteration = 0	
	

	while(stop_condition >= tol):
		iteration += 1
		x1 = ( a * f(b) - b * f(a) ) / (f(b) - f(a))
		stop_condition = max(b-x1, x1-a )
		result = f(x1)
		
		print(f"{str(iteration).zfill(2)}. iteration:    " + f" x = {x1}".ljust(30)  +  f" F(x) = {result}")
		
		if (result == 0):
			return x1;
	
		# yeni kok aralıgını belirle
		if (f(a) < 0 and result < 0):
			a = x1
		elif(f(a) > 0 and result > 0):
			a = x1
		else:
			b = x1

		
	return x1
		




if __name__ == "__main__":	
	print(regula_falsi(0.5, math.pi/4, 10**-3))

