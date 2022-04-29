import math 
import matplotlib.pyplot as plt
import numpy as np

X_1 = [i*math.pi/8 for i in range(6)]
X_2 = [0, math.pi/8, math.pi/3, 3*math.pi/8]
X_ = 3*math.pi/16

def f(x):
	return math.tan(x) + x

def f_omega(x):
	mas = [1 for i in range(len(x))]
	for i in range(len(x)):
		x_ = x[i]
		for j in range(len(x)):
			if i != j:
				mas[i]*=(x_ - x[j])
		mas[i] = f(x[i])/mas[i]
	return mas

def Lagrange(x, x_, mas):
	y = 0
	for i in range(len(mas)):
		lamb = mas[i]
		for j in range(len(mas)):
			if i != j:
				lamb *= (x - x_[j])
		y += lamb
	return y

def tabl(x):
	mas = [[] for i in range(len(x)+1)]
	mas[0] = x

	for i in range(len(x)):
		mas[1].append(f(x[i]))

	for i in range(2, len(mas)):
		for j in range(len(mas[i-1])-1):
			mas[i].append((mas[i-1][j]-mas[i-1][j+1])/(x[j]-x[j+i-1]))

	return mas

def newton(x, mas):
	y = 0
	for i in range(1, len(mas) - 1):
		lamb = mas[i+1][0]
		for j in range(i):
			lamb *= (x - mas[0][j])
		y+=lamb

	return y

print(Lagrange(X_, X_1, f_omega(X_1)), math.tan(X_) + X_)
print(newton(X_, tabl(X_1)), math.tan(X_) + X_)
print(Lagrange(X_, X_2, f_omega(X_2)), math.tan(X_) + X_)
print(newton(X_, tabl(X_2)), math.tan(X_) + X_)

def plot_1(x):
	mas = f_omega(x)
	Y = []
	for i in range(len(x)):
		Y.append(f(x[i]))
	plt.scatter(x, Y, color='purple')
	float_range_array = np.arange(x[0], x[-1]+0.1, 0.1)
	r = list(float_range_array)
	Y = []
	for i in r:	
		Y.append(Lagrange(i, x, mas))
	plt.plot(r, Y, color='orange')
	plt.show()

def plot_2(x):
	mas = tabl(x)
	Y = []
	for i in range(len(x)):
		Y.append(f(x[i]))
	plt.scatter(x, Y, color='purple')
	float_range_array = np.arange(x[0], x[-1]+0.1, 0.1)
	r = list(float_range_array)
	Y = []
	for i in r:	
		Y.append(newton(i, mas))
	plt.plot(r, Y, color='yellow')
	plt.show()

plot_1(X_1)
plot_2(X_1)
plot_1(X_2)
plot_2(X_2)
