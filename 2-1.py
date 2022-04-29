import math 

def norm_1(x, x_1):
	return abs(x - x_1)

def prov(x_1):
	if (x_1 ** 3 - 2 * x_1 ** 2  - 10 * x_1 + 15) * (6 * x_1 - 4) > 0:
		return 1
	else:
		return 0

def Nfunc(x):
	k_1 = x ** 3 - 2 * x ** 2  - 10 * x + 15
	k_2 = 3 * x ** 2 - 4 * x - 10
	return -k_1/k_2

def newton(x_1, eps):
	num = x_1
	it = 0
	e = 1
	if not prov(x_1):
		print('error change x_1')
	else:
		while(e > eps):
			it+=1
			x = x_1
			x_1 += Nfunc(x_1)
			e = norm_1(x, x_1)
			print('iter - ', it, 'x = ', x_1, ' norm = ', e)
	if x_1 < 0:
		print('your answer < 0')
		if num < 0:
			x_1 = num + 10 ** (len(str(num)) - 1)
		else:
			x_1 = num + 10 ** len(str(num))
		print('new x_1 = ', x_1)
		newton(x_1, eps)

def pfunk(x):
	return math.sqrt(10 + 5/(x-2))

def ppfunk(x):
	return -2.5 / math.sqrt((10*x-15) * (x-2)**3)

def norm_2(a, b):
	if abs(ppfunk(a)) > abs(ppfunk(b)):
		return abs(ppfunk(a))
	else: return abs(ppfunk(b))

def simple_it(a, b, eps):
	it = 0
	q = norm_2(a, b)
	q = q/(1-q)
	e = q * norm_1(a, b)
	x = (a+b)/2
	while(e > eps):
		it+=1
		x_1 = pfunk(x)
		e =  q * norm_1(x, x_1)
		print('iter - ', it, 'x = ', x_1, ' norm = ', e)
		x = x_1

def main():
	eps = float(input('Enter eps:'))
	while(eps < 1):
		x = float(input('Enter x for Newton method:'))
		print('Newton')
		newton(x, eps)
		print('Simple iteration')
		simple_it(3, 4, eps)
		eps = float(input('Enter eps:'))

main()
