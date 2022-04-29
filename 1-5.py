import cmath
import math
import numpy as np
import tkinter as tk
from tkinter import *
import threading 

A = np.array([[2, -4, 5],[-5, -2, -3],[1, -8, -3]])
n = len(A)

def find_v(a, n):
	v = [[a[i][n]] for i in range(len(a))]
	g = 0
	for i in range(n, len(a)):
		g += a[i][n] ** 2
	v[n][0] += np.sign(v[n][0]) * math.sqrt(g)
	for i in range(n):
		v[i][0] = 0

	return np.array(v)

def find_housholder(a, n):
	v = find_v(a, n)
	v_t = v.transpose()
	vv_t = np.dot(v, v_t)
	v_tv = np.dot(v_t, v)

	return np.eye(len(a)) - 2 / v_tv[0][0] * vv_t

def find_QR(a):
	R = a.copy()
	Q = np.eye(len(a))
	for i in range(len(R) - 1):
		H = find_housholder(R, i)
		Q = np.dot(Q, H)
		R = np.dot(H, R)
	return Q, R

def norm(a):
	s = 0
	for i in range(len(a)):
		for j in range(len(a)):
			if j == 0 and i > j:
				s += a[i][j] ** 2
	return math.sqrt(s)

def QRmethod(a, eps):
	it = 0
	A_ = a.copy()
	e = norm(A_)
	while(e > eps):
		it += 1
		Q, R = find_QR(A_)
		A_ = np.dot(R, Q)
		e = norm(A_)

	return A_, it

def solve_roots(a):
    res = [a[0][0]]
    b = a[2][2]+a[1][1]
    D = b ** 2 - 4 * (a[1][1]*a[2][2] - a[1][2] * a[2][1])
    b = -(a[2][2]+a[1][1])/2
    res.append(b + cmath.sqrt(D)/2)
    res.append(b - cmath.sqrt(D)/2)

    return res

def make_window():
	window = tk.Tk()
	window.title("Окно управления")
	window.geometry('200x270')
	text_var = []
	entries = []

	def ButtonCall1():
		eps1 = float(eps.get())
		a, it = QRmethod(A, eps1)
		print('Количество итераций: ', it)
		print('Матрица А:')
		print(a)
		print('Решения:')
		print(solve_roots(a))
		
	button = tk.Button(window, text="14 Вариант", command=ButtonCall1)
	button.place(x=65, y=150)

	def get_mat():
		eps1 = float(eps.get())
		own_arr = []
		for i in range(n):
			own_arr.append([])
			for j in range(n):
				own_arr[i].append(int(text_var[i][j].get()))
		own_arr = np.array(own_arr)
		eps1 = float(eps.get())
		a, it = QRmethod(own_arr, eps1)
		print('Количество итераций: ', it)
		print('Матрица А:')
		print(a)
		print('Решения:')
		res = solve_roots(a)
		res[0][0] = res[0][0] / 10
		print(res)


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

	button = tk.Button(window, text="Собственные условия", command=get_mat)
	button.place(x=35, y=180)

	eps = StringVar()
	ent = Entry(window, textvariable=eps, width=7)

	label_accuracy1 = tk.Label(window, text="eps")
	label_accuracy1.place(x=50, y=220)
	ent.place(x=90, y=220)

	tk.mainloop()

def main():
    t1 = threading.Thread(target=make_window)
    t1.start()

main()