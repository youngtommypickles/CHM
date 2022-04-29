import math 
import matplotlib.pyplot as plt
import numpy as np

#C = [[0.9*i for i in range(-1, 5, 1)],[-1.2689, 0, 1.2689, 2.6541, 4.4856, 9.9138]]
C = [[1.7*i for i in range(0, 6)],[0, 1.3038, 1.8439, 2.2583, 2.6077, 2.9155]]
#C = [[0.9*i for i in range(6)], [math.cos(0.9*i*math.pi) - (math.sqrt(0.9*i*math.pi)) for i in range(6)]]

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

def func(x, A):
	f = 0
	for i in range(len(A)):
		f += A[i]*(x**i)
	return f

def error(C, A):
	err = 0
	for i in range(len(C[0])):
		err += (func(C[0][i], A) - C[1][i])**2
	return err

def plot(C, eps):
	float_range_array = np.arange(C[0][0], C[0][-1]+eps*(C[0][1]-C[0][0]), eps*(C[0][1]-C[0][0]))
	x = list(float_range_array)
	plt.scatter(C[0], C[1], color='purple')
	col = ['orange', 'yellow', 'green', 'blue', 'purple', 'red']
	j = 0
	for i in [2, 3, 4, 5, 6, 7]:
		arr, y = create_table(i, C)
		a = np.linalg.solve(arr, y)
		print(col[j], 'цвет - коэффиценты многочлен', i-1, 'степень:', a)
		print('Ошибка -', error(C, a))
		Y = []
		for i in x:
			Y.append(func(i, a))
		plt.plot(x, Y, color=col[j])
		j += 1
	plt.show()

plot(C, 0.01)
