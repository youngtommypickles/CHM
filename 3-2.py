import math 
import matplotlib.pyplot as plt
import numpy as np

C = [[0.9*i for i in range(5)], [0, 0.72235, 1.5609, 2.8459, 7.7275]]
#C = [[0.9*i for i in range(7)], [0, 0.72235, 1.5609, 2.8459, 7.7275, 16.33, 28.332]]
#C = [[0.9*i for i in range(7)], [0, 0.72235, 1.5609, 2.8459, 7.7275, 16.33, 12]]
#C = [[0.9*i for i in range(10)], [math.cos(0.9*i*math.pi) - (math.sqrt(0.9*i*math.pi)) for i in range(10)]]
X_ = 1.5

def h(i, x):
	return x[i] - x[i-1]

def system(x):
	n = len(x[0])-1
	arr = [[0 for i in range(len(x[0])-2)] for i in range(len(x[0])-2)]
	y = [[0] for i in range(len(x[0])-2)]
	arr[0][0] = 2*(h(1, x[0]) + h(2, x[0]))
	arr[0][1] = h(2, x[0])
	y[0][0] = 3*((x[1][2]-x[1][1])/h(2, x[0]) - (x[1][1]-x[1][0])/h(1, x[0]))
	for i in range(1, len(arr) - 1):
		arr[i][i-1] = h(i, x[0])
		arr[i][i] = 2*(h(i, x[0]) + h(i+1, x[0]))
		arr[i][i+1] = h(i+2, x[0])
		y[i][0] = 3*((x[1][i+2]-x[1][i+1])/h(i+2, x[0]) - (x[1][i+1]-x[1][i])/h(i+1, x[0]))
	arr[-1][-2] = h(n-1, x[0])
	arr[-1][-1] = 2*(h(n-1, x[0])+h(n, x[0]))
	y[-1][0] = 3*((x[1][n]-x[1][n-1])/h(n, x[0]) - (x[1][n-1]-x[1][n-2])/h(n-1, x[0]))

	return np.array(arr), np.array(y)

def qui(a, d):
	new_a = [[0 for i in range(len(a))] for i in range(len(a))]
	new_d = [[0] for i in range(len(a))]
	for i in range(len(a)):
		for j in range(len(a)):
			if i != j:
				new_a[i][j] = -1*a[i][j]/a[i][i]
		new_d[i][0] = d[i][0]/a[i][i]

	return np.array(new_a), np.array(new_d)

def norm(a):
	_max = 0
	for i in range(len(a)):
		delt = 0
		for j in range(len(a[0])):
			delt+=abs(a[i][j])
		if delt > _max:
			_max = delt
	return _max

def simple_iterations(ar, d, e):
	num = 0
	eps = 1
	a, b = qui(ar, d)
	koef = norm(a)/(1-norm(a))
	if 1 < norm(a):
		print("error")
		return 0, 0
	x = b.copy()
	while(eps > e):
		num+=1
		xk = b + np.dot(a,x)
		eps = koef * norm(x-xk)
		x = xk.copy()
	return x

arr, y = system(C)
c = simple_iterations(arr, y, 0.001)
print(c)

def create_table(x, c):
	arr = [[0 for i in range(len(x[0])-1)] for i in range(len(x[0]) - 1)]
	arr[2][0] = 0
	for i in range(len(c)):
		arr[2][i+1] = c[i][0]
	for i in range(len(x[0])-1):
		arr[0][i] = x[1][i]
	for i in range(len(x[0])-2):
		arr[1][i] = (x[1][i+1]-x[1][i])/h(i+1, x[0]) - 1/3 * h(i+1, x[0]) * (arr[2][i+1] + 2*arr[2][i])
		arr[3][i] = (arr[2][i+1] - arr[2][i])/(3*h(i+1, x[0]))
	arr[1][-1] = (x[1][-1]-x[1][-2])/h(len(x[0]) - 1, x[0]) -2/3 * h(len(x[0]) - 1, x[0]) * arr[2][-1]
	arr[3][-1] = - arr[2][-1]/(3* h(len(x[0]) - 1, x[0]))
	return arr

arr = create_table(C, c)
print(arr)

def func(x, c, A):
	summ = 0
	for i in range(len(c[0])-1):
		if x >= c[0][i] and x <= c[0][i+1]:
			break
	x_ = x - c[0][i]
	for j in range(len(A)):
		summ += A[j][i]*(x_)**j
	return summ

def plot(c, arr):
	plt.scatter(c[0], c[1], color='purple')
	col = ['orange', 'yellow', 'blue', 'green', 'red']
	j = 0
	for i in [c[0][-1]/100, c[0][-1]/10, c[0][-1]/5, c[0][-1]/2, c[0][-1]]:
		float_range_array = np.arange(0, c[0][-1]+0.1, i)
		x = list(float_range_array)
		Y = []
		for i in range(len(x)):
			Y.append(func(x[i], c, arr))
		plt.plot(x, Y, color=col[j])
		j+=1
	
	plt.show()

plot(C, arr)