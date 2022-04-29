import math 

def mat(n, x_1, x_2):
	mat = [[0, 0], [0, 0]]
	mat[0][0] = 2/9 * x_1
	mat[0][1] = 8/9 * x_2
	mat[1][0] = -math.exp(x_1)
	mat[1][1] = 3

	if n == 1:
		mat[0][0] = x_1 ** 2 / 9 + x_2 ** 2 / 2.25 - 1
		mat[1][0] = 3 * x_2 - math.exp(x_1)
	if n == 2:
		mat[0][1] = x_1 ** 2 / 9 + x_2 ** 2 / 2.25 - 1
		mat[1][1] = 3 * x_2 - math.exp(x_1)

	return mat

def det(mat):
	return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]

def norm(x, y, x_1, y_1):
	if abs(x-x_1) > abs(y-y_1):
		return abs(x-x_1)
	else: return abs(y-y_1)

def newton(x_1, x_2, eps):
	e = 1
	it = 0
	while(e > eps):
		detJ = det(mat(0, x_1, x_2))
		detA_1 = det(mat(1, x_1, x_2))
		detA_2 = det(mat(2, x_1, x_2))
		x = x_1
		y = x_2
		x_1 = x_1 - detA_1/detJ
		x_2 = x_2 - detA_2/detJ
		it += 1
		e = norm(x, y, x_1, x_2)
		print('iter - ', it, 'x_1 = ', x_1, 'x_2 = ', x_2, ' norm = ', e)

def qhi_p(x_1, x_2):
	mat = [[0, 0], [0, 0]]
	mat[0][0] = 0
	mat[0][1] = 1 / x_2 
	mat[1][0] = - 3 * x_1 / (4 * (9 - x_1 ** 2))
	mat[1][1] = 0

	return mat

def qhi(x_1, x_2):
	return math.log(3*x_2), math.sqrt(2.25 * (1 - x_1 ** 2 / 9))

def find_q(mat):
	if abs(mat[0][0]) + abs(mat[0][1]) > abs(mat[1][0]) + abs(mat[1][1]):
		return abs(mat[0][0]) + abs(mat[0][1])
	else: return abs(mat[1][0]) + abs(mat[1][1])

def simple_it(x_1, x_2, eps):
	it = 0
	mat = qhi_p(x_1, x_2)
	q = find_q(mat)
	k = q/(1-q)
	e = 1
	while(e > eps):
		it+=1
		x = x_1
		y = x_2
		x_1 = math.log(3*x_2)
		x_2 = math.sqrt(2.25 * (1 - x_1 ** 2 / 9))
		e = norm(x, y, x_1, x_2)
		print('iter - ', it, 'x_1 = ', x_1, 'x_2 = ', x_2, ' norm = ', e)

def main():
	eps = float(input('Enter eps:'))
	while(eps < 1):
		x_1 = float(input('Enter x_1, x_1 lies (1, 1.5):'))
		x_2 = float(input('Enter x_2, x_2 lies (1, 1.5):'))
		print('Newton')
		newton(x_1, x_2, eps)
		print('Simple iteration')
		simple_it(x_1, x_2, eps)
		eps = float(input('Enter eps:'))

main()
