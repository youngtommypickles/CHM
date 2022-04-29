import math 
import matplotlib.pyplot as plt
import numpy as np

X0 = 0
X1 = 2
true_value = (np.log(3) + 2*np.arctan(0.5))/256
#X0 = -1
#X1 = 1

def func(x):
	return 1/(x**4+16)#x/((3*x+4)**2)

def rungerombergerror(f1, f2, h1, h2, p):
	k = max(h1/h2, h2/h1)
	print('Ошибка Рунге-Ромберга:', (f2-f1)/(k**p - 1))
	print('Точность_1:', f1+(f2-f1)/(k**p - 1))
	print('Точность_2:', f2+(f2-f1)/(k**p - 1))

def create_table(n, C):
	arr = [[0 for i in range(n)] for i in range(n)]
	arr_y = [0 for i in range(n)]
	y = 0
	for i in range(n):
		l = i
		for j in range(n):
			for k in C[0]:
				arr[i][j] += k**l 
			l+=1
	for i in range(n):
		for j in range(len(C[0])):
			arr_y[i] += C[1][j]*(C[0][j]**i)
	return np.array(arr), np.array(arr_y)

def func_2(x, A):
	f = 0
	for i in range(len(A)):
		f += A[i]*(x**i)
	return f

def rectangle_plot(h):
	summ = 0
	Y = []
	float_range_array = np.arange(X0, X1+0.01, 0.01)
	x = list(float_range_array)
	for i in x:
		Y.append(func(i))
	plt.plot(x, Y, color='red')
	Y = []
	float_range_array = np.arange(X0, X1+h, h)
	x = list(float_range_array)
	for i in range(len(x)-1):
		y = func((x[i]+x[i+1])/2)
		plt.plot([x[i], x[i], x[i+1], x[i+1]], [0, y, y, 0], color = 'blue')
		plt.plot([x[i], x[i+1]], [0, 0],  color='black')
		summ += h*y
	print('шаг - ', h, ':ответ методом прямоугольников:', summ)
	plt.show()
	return summ

def trapezoid_plot(h):
	summ = 0
	Y = []
	float_range_array = np.arange(X0, X1+0.01, 0.01)
	x = list(float_range_array)
	for i in x:
		Y.append(func(i))
	plt.plot(x, Y, color='red')
	Y = []
	float_range_array = np.arange(X0, X1+h, h)
	x = list(float_range_array)
	for i in range(len(x)-1):
		y_1 = func((x[i]))
		y_2 = func((x[i+1]))
		plt.plot([x[i], x[i], x[i+1], x[i+1]], [0, y_1, y_2, 0], color = 'blue')
		plt.plot([x[i], x[i+1]], [0, 0],  color='black')
		summ += (y_1+y_2)*h
	summ/=2
	print('шаг - ', h, ':ответ методом трапеций:', summ)
	plt.show()
	return summ

def simpson_plot(h):
	summ = 0
	Y = []
	float_range_array = np.arange(X0, X1+0.01, 0.01)
	x = list(float_range_array)
	for i in x:
		Y.append(func(i))
	plt.plot(x, Y, color='red')
	Y = []
	float_range_array = np.arange(X0, X1+h, h)
	print(float_range_array)
	x = list(float_range_array)
	for i in range(0, len(x)-1, 1):
		y_1 = func((x[i]))
		y_2 = func((x[i+1]))
		y_12 = func((x[i]+x[i+1])/2)
		plt.plot([x[i], x[i]], [0, y_1], color = 'blue')
		arr, y = create_table(3, [[x[i], (x[i]+x[i+1])/2 ,x[i+1]],[y_1, y_12, y_2]])
		a = np.linalg.solve(arr, y)
		float_range_array = np.arange(x[i], x[i+1]+0.01, 0.01)
		x_2 = list(float_range_array)
		Y_2 = []
		for j in x_2:
			Y_2.append(func_2(j, a))
		plt.plot(x_2, Y_2, color = 'blue')
		plt.plot([x[i+1], x[i+1]], [y_2, 0], color = 'blue')
		plt.plot([x[i], x[i+1]], [0, 0],  color='black')
		summ += (y_1+4*y_12+y_2)*h
	summ/=6
	print('шаг - ', h, ':ответ методом Симпсона:', summ)
	plt.show()
	return summ

def plot(method, h1, h2, p):
	f1 = method(h1)
	f2 = method(h2)
	error = rungerombergerror(f1, f2, h1, h2, p)

plot(rectangle_plot, 0.5, 0.25, 2)
plot(trapezoid_plot, 0.5, 0.25, 2)
plot(simpson_plot, 0.5, 0.25, 4)