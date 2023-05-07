import math

def f(x):
	return (0.5 * math.pi -  math.asin(x) - x*(1- x**2)**0.5) - 1.24
	

# derative of func f
def fd(x):
	return -2* (1-x**2)**0.5



def bisection(a, b, hata):
	if (f(a) * f(b) > 0 ):
		print("aralikta kök yok")
		return -1
	
		
	iteration = 0	
	durma_kosulu = hata + 1 # donguye girebilmek icin
	

	while(durma_kosulu >= hata):

		iteration += 1
		durma_kosulu = (b-a) / (2**iteration)
		orta_nokta = (a+b) / 2
		sonuc = f(orta_nokta)
		

		#print(f"{str(iteration).zfill(2)}. iteration values:    " + f" a = {a}".ljust(30)  +  f" b = {b}".ljust(30) +  f" F(x) = {sonuc}".ljust(35) + f" durma_kosulu = {durma_kosulu}".ljust(20))

		
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
		
	
	
# regula_falsi
def regula_falsi(a, b, hata):
	if (f(a) * f(b) > 0 ):
		print("aralikta kök yok")
		return -1
		# gercek kok bilinmiyor
		
	durma_kosulu = hata + 1  # donguye girebilmek icin
	iteration = 0	
	

	while(durma_kosulu >= hata):
		iteration += 1
		x1 = ( a * f(b) - b * f(a) ) / (f(b) - f(a))
		durma_kosulu = max(b-x1, x1-a )
		sonuc = f(x1)
		
		#print(f"{str(iteration).zfill(2)}. iteration values:    " + f" a = {a}".ljust(30)  +  f" b = {b}".ljust(30) +  f" F(x) = {sonuc}".ljust(35) + f" durma_kosulu = {durma_kosulu}".ljust(20))
		
		if (sonuc == 0):
			return x1;
	
		# yeni kok aralıgını belirle
		if (f(a) < 0 and sonuc < 0):
			a = x1
		elif(f(a) > 0 and sonuc > 0):
			a = x1
		else:
			b = x1

		
	return x1
		



def newton_raphson(a, b, tolerans):
	if (f(a) * f(b) > 0 ):
		print("aralikta kök yok")
		return -1
	
	x1 = a  				# sonsuz donguye giriyorsa a yerine b den basla
	
	diff = tolerans + 1 	# donguye girebilmek icin gecici atama
	iteration = 0
	
	while (diff > tolerans):
		iteration += 1
		x0 = x1;
		x1 = x0 - f(x0) / fd(x0)
	
		result = f(x1)
		diff = abs(x0 - x1)

		#print(f"{str(iteration).zfill(2)}. iteration values:    " + f"stop_condition = {diff}".ljust(42) + f" F(x1) = {result}".ljust(35) + f"x1_value = {x1}")
		
			
	return x1




if __name__ == "__main__":	
	print(bisection(0.1, 0.9, 10**-3))
	print(regula_falsi(0.1, 0.9, 10**-3))
	print(newton_raphson(0.1,0.9, 10**-6))

