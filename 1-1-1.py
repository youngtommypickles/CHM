import tkinter as tk
from tkinter import *
import threading 
import numpy as np

arr = [[-1,-3, -4, 0],[3, 7, -8, 3], [1, -6, 2, 5],[-8, -4, -1, -1]]
d = [-3, 30, -90, 12]

def funcLU(a):
    U = [[0 for i in range(len(a))] for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            U[i][j] = a[i][j]
    L = [[0 for i in range(len(a))] for i in range(len(a))]

    for i in range(len(a)):
        for k in range(i+1,len(a)):
            L[k][i] = U[k][i]/U[i][i]
            for j in range(i,len(a)):
                U[k][j] = U[k][j] - L[k][i] * U[i][j]
        L[i][i] = 1     

    return L, U

def solve(L, U, d):
    x, y = [0 for i in range(len(L))], [0 for i in range(len(U))]

    y[0] = d[0]
    for i in range(1, len(L)):
        y[i] = d[i]
        for j in range(i):
            y[i]-=L[i][j]*y[j]

    x[len(U)-1] = (y[len(U)-1]/U[len(U)-1][len(U)-1])
    for i in range(len(U)-2, -1, -1):
        x[i] = y[i]
        for j in range(len(L)-1, i, -1):
            x[i]-=U[i][j]*x[j]
        x[i] = (x[i]/U[i][i])
    return x

def det(a):
    L, U = funcLU(a)
    d = 1
    for i in range(len(U)):
        d*=U[i][i]
    return d

def obr(a):
    b = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    for k in range(len(a)):
        if abs(a[k][k]):
            for i in range(k+1, len(a)):
                if abs(a[i][k]) > abs(a[k][k]):
                    for j in range(k, len(a)):
                        a[k][j], a[i][j] = a[i][j], a[k][j]
                        b[k][j], b[i][j] = b[i][j], b[k][j]
                    b[k], b[i] = b[i], b[k]
                    break
        p = a[k][k]
        for j in range(k, len(a)):
            a[k][j] /= p
            b[k][j] /= p
        for i in range(len(a)):
            if i == k or a[i][k] == 0: continue
            f = a[i][k]
            for j in range(k, len(a)):
                a[i][j] -= f * a[k][j]
                b[i][j] -= f * b[k][j]

    return b

def make_window():
    window = tk.Tk()
    window.title("Окно управления")
    window.geometry('320x320')
    text_var = []
    entries = []

    def ButtonCall1():
        detr = det(arr)
        print("Определитель:", detr)
        L, U = funcLU(arr)
        L1 = np.array(L)
        print("L-матрица")
        print(L1)
        U1 = np.array(U)
        print("U-матрица")
        print(U1)
        x = solve(L, U, d)
        a = [[0 for i in range(len(arr))] for i in range(len(arr))]
        for i in range(len(arr)):
            for j in range(len(arr)):
                a[i][j] = arr[i][j]
        A_1 = np.array(obr(a))
        print("Обратная-матрица:")
        print(A_1)
        print("Ответ: x =", x)

    button = tk.Button(window, text="14 Вариант", command=ButtonCall1)
    button.place(x=130, y=200)

    def get_mat():
        own_arr = []
        own_d = []
        for i in range(len(arr)):
            own_arr.append([])
            for j in range(len(arr)):
                own_arr[i].append(int(text_var[i][j].get()))
        for i in range(len(arr)):
            own_d.append(int(d_var[i].get()))
        print(own_arr)
        print(d)
        detr = det(own_arr)
        print("Определитель:", detr)
        L, U = funcLU(own_arr)
        L1 = np.array(L)
        print("L-матрица")
        print(L1)
        U1 = np.array(U)
        print("U-матрица")
        print(U1)
        x = solve(L, U, own_d)
        a = [[0 for i in range(len(own_arr))] for i in range(len(own_arr))]
        for i in range(len(own_arr)):
            for j in range(len(own_arr)):
                a[i][j] = own_arr[i][j]
        A_1 = np.array(obr(a))
        print("Обратная-матрица:")
        print(A_1)
        print("Ответ: x =", x)
        own_arr = []
        own_d = []
        print(x)

    x2, y2 = 0, 0
    for i in range(len(arr)):
        text_var.append([])
        entries.append([])
        for j in range(len(arr)):
            text_var[i].append(StringVar())
            entries[i].append(Entry(window, textvariable=text_var[i][j],width=3))
            entries[i][j].place(x=60 + x2, y=50 + y2)
            x2 += 30

        y2 += 30
        x2 = 0

    y2 = 0
    d_var = []
    d_var1 = []
    for i in range(len(arr)):
        d_var.append(StringVar())
        d_var1.append(Entry(window, textvariable=d_var[i],width=3))
        d_var1[i].place(x = 240, y=50 + y2)
        y2 += 30

    button = tk.Button(window, text="Собственные условия", command=get_mat)
    button.place(x=100, y=240)

    tk.mainloop()


def main():
    t1 = threading.Thread(target=make_window)
    t1.start()

main()