#!/bin/python3

import math

def f(x):
	return (0.5 * math.pi -  math.asin(x) - x*(1- x**2)**0.5) - 1.24
	


def bisection(a, b, tol):
	if (f(a) * f(b) > 0 ):
		print("aralikta kök yok")
		return -1
	
		
	iteration = 0	
	stop_condition = tol + 1 # donguye girebilmek icin
	

	while(stop_condition >= tol):

		iteration += 1
		stop_condition = (b-a) / (2**iteration)
		orta_nokta = (a+b) / 2
		sonuc = f(orta_nokta)
		

		print(f"{str(iteration).zfill(2)}. iteration values:    " + f" a = {a}".ljust(30)  +  f" b = {b}".ljust(30) +  f" F(x) = {sonuc}".ljust(35) + f" durma_kosulu = {stop_condition}".ljust(20))

		
		if (sonuc == 0):
			return orta_nokta;

		# yeni kok aralıgını belirle
		if (f(a) < 0 and sonuc < 0):
			a = orta_nokta
		elif(f(a) > 0 and sonuc > 0):
			a = orta_nokta
		else:
			b = orta_nokta

		
	return orta_nokta
		
	


if __name__ == "__main__":	
	print(bisection(0.1, 0.9, 10**-3))
	