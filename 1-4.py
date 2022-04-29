import numpy as np
import tkinter as tk
from tkinter import *
import threading 
import math

arr = np.array([[-7, -5, -9], [-5, 5, 2], [-9, 2, 9]])
n = len(arr)

def maxij(a):
	_max = 0
	_i = 0
	_j = 0
	for i in range(len(a)):
		for j in range(len(a)):
			if i != j:
				if _max < abs(a[i][j]):
					_max = abs(a[i][j])
					_i = i
					_j = j 
	return _i, _j

def norm(a):
	_max = (a[0][1]**2 + a[0][2]**2 + a[1][2]**2)**(0.5)
	return _max

def mat_rotation(a, i, j):
	if a[i][i] == a[j][j]:
		phi = math.pi/4
	else:
		phi = 0.5 * np.arctan((2*a[i][j])/(a[i][i] - a[j][j]))
	E = np.eye(len(a))
	E[i][i] = np.cos(phi)
	E[j][j] = np.cos(phi)
	E[i][j] = -np.sin(phi)
	E[j][i] = np.sin(phi)
	return E

def jacobi_rotation_method(a, e):
	_a = a.copy()
	E = np.eye(len(a))
	_eps = 1
	num = 0
	while(_eps > e):
		num+=1
		i, j = maxij(_a)
		U_1 = mat_rotation(_a, i, j)
		E = np.dot(E, U_1)
		_a = np.dot(np.transpose(U_1), _a)
		_a = np.dot(_a, U_1)
		_eps = norm(_a)
	return E, _a, num

def make_window():
	window = tk.Tk()
	window.title("Окно управления")
	window.geometry('200x270')
	text_var = []
	entries = []

	def ButtonCall1():
		eps1 = float(eps.get())
		U, a, num = jacobi_rotation_method(arr, eps1)
		print("Матрица:")
		print(a)
		print("Собственные значения:")
		for i in range(len(a)):
			print("Лямбда", i , " = ",a[i][i])
		print("Собственные вектора:")
		U = np.transpose(U)
		for i in range(len(a)):
			print("x", i, " = ", U[i])
		print("Количество итераций: ", num)

	button = tk.Button(window, text="14 Вариант", command=ButtonCall1)
	button.place(x=65, y=150)

	def get_mat():
		eps1 = float(eps.get())
		own_arr = []
		for i in range(n):
			own_arr.append([])
			for j in range(n):
				own_arr[i].append(int(text_var[i][j].get()))
		U, a, num = jacobi_rotation_method(own_arr, eps1)
		print("Матрица:")
		print(a)
		print("Собственные значения:")
		for i in range(len(a)):
			print("Лямбда", i , " = ",a[i][i])
		print("Собственные вектора:")
		U = np.transpose(U)
		for i in range(len(a)):
			print("x", i, " = ", U[i])
		print("Количество итераций: ", num)
		own_arr = []


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