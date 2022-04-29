import numpy as np
import tkinter as tk
from tkinter import *
import threading 

arr = np.array([[-22, -2, -6, 6], [3, -17, -3, 7], [2, 6, -17, 5], [-1, -8, 8, 23]])
#arr = np.array([[12, -3, -1, 3], [5, 20, 9, 1], [6, -3, -21, -7], [8, -7, 3, -27]])
d = np.array([[96], [-26], [35], [-234]])
#d = np.array([[-31], [90], [119], [-234]])
e = 0.01
n = len(arr)

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

def norm2(a):
	_max = 0
	for i in range(len(a)):
		if _max < abs(a[i]):
			_max = abs(a[i])
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
	return x, num

def seidel(ar, d, e):
	num = 0
	eps = 1
	a, b = qui(ar, d)
	koef = norm(a)/(1-norm(a))
	if 1 < norm(a):
		print("error")
		return 0, 0
	xk = b.copy()
	x = b.copy()
	while(eps > e):
		num+=1
		xk = x.copy()
		for i in range(len(ar)):
			xk[i] = b[i] + np.dot(a[i], xk)
		eps = koef * (norm(x-xk))
		x = xk.copy()
	return xk, num

def make_window():
	window = tk.Tk()
	window.title("Окно управления")
	window.geometry('320x320')
	text_var = []
	entries = []

	def ButtonCall1():
		eps1 = float(eps.get())
		x1, num1 = simple_iterations(arr, d, eps1)
		x2, num2 = seidel(arr, d, eps1)
		print("Метод простых итераций")
		print("Ответы")
		print(x1)
		print("Итерации:", num1)
		print("Метод Зейделя")
		print("Ответы")
		print(x2)
		print("Итерации:", num2)

	button = tk.Button(window, text="14 Вариант", command=ButtonCall1)
	button.place(x=130, y=200)

	def get_mat():
		eps1 = float(eps.get())
		own_arr = []
		own_d = [[] for i in range(n)]
		for i in range(n):
			own_arr.append([])
			for j in range(n):
				own_arr[i].append(int(text_var[i][j].get()))
		for i in range(n):
			own_d[i].append(int(d_var[i].get()))

		own_ar = np.array(own_arr)
		own_dd = np.array(own_d)
		x1, num1 = simple_iterations(own_ar, own_dd, eps1)
		x2, num2 = seidel(own_ar, own_dd, eps1)
		print("Метод простых итераций")
		print("Ответы")
		print(x1)
		print("Итерации:", num1)
		print("Метод Зейделя")
		print("Ответы")
		print(x2)
		print("Итерации:", num2)

	x2, y2 = 0, 0
	for i in range(n):
		text_var.append([])
		entries.append([])
		for j in range(n):
			text_var[i].append(StringVar())
			entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))
			entries[i][j].place(x=60 + x2, y=50 + y2)
			x2 += 30

		y2 += 30
		x2 = 0

	y2 = 0
	d_var = []
	d_var1 = []
	for i in range(n):
		d_var.append(StringVar())
		d_var1.append(Entry(window, textvariable=d_var[i],width=3))
		d_var1[i].place(x = 240, y=50 + y2)
		y2 += 30

	button = tk.Button(window, text="Собственные условия", command=get_mat)
	button.place(x=100, y=240)

	eps = StringVar()
	ent = Entry(window, textvariable=eps, width=7)

	label_accuracy1 = tk.Label(window, text="eps")
	label_accuracy1.place(x=120, y=290)
	ent.place(x=150, y=290)
	

	tk.mainloop()

def main():
    t1 = threading.Thread(target=make_window)
    t1.start()

main()
