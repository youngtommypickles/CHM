import tkinter as tk
from tkinter import *
import threading 

n = 5

arr = [[-1,-1, 0, 0, 0],[7, -17, -8, 0, 0], [0, -9, 19, 8, 0],[0, 0, 7, -20, 4], [0, 0, 0, -4, 12]]
d = [-4, 132, -59, -193, -40]

def func(a, d, P, Q, n):
    '''Прямой обход'''
    P[0] = -a[0][1]/a[0][0]
    Q[0] = d[0]/a[0][0]
    for i in range(1, n-1, 1):
        P[i] = -a[i][i+1]/(a[i][i]+a[i][i-1]*P[i-1])
        Q[i] = (d[i]-a[i][i-1]*Q[i-1])/(a[i][i]+a[i][i-1]*P[i-1])
    P[n-1] = 0
    Q[n-1] = (d[n-1] - a[n-1][n-2]*Q[n-2])/(a[n-1][n-1]+a[n-1][n-2]*P[n-2])

    '''Обратный обход'''
    d[n-1] = (Q[n-1])
    for i in range(n-2, -1, -1):
        d[i] = (P[i]*d[i+1] + Q[i])
    return d

def make_window():
    window = tk.Tk()
    window.title("Окно управления")
    window.geometry('320x320')
    text_var = []
    entries = []

    def ButtonCall1():
        ap = arr.copy()
        dd = d.copy()
        x = func(ap, dd, [0 for i in range(n)], [0 for i in range(n)], n)
        print(x)

    button = tk.Button(window, text="14 Вариант", command=ButtonCall1)
    button.place(x=130, y=200)

    def get_mat():
        own_arr = []
        own_d = []
        for i in range(n):
            own_arr.append([])
            for j in range(n):
                own_arr[i].append(int(text_var[i][j].get()))
        for i in range(n):
            own_d.append(int(d_var[i].get()))
        x = func(own_arr, own_d, [0 for i in range(n)], [0 for i in range(n)], n)
        own_arr = []
        own_d = []
        print(x)

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

    tk.mainloop()

def main():
    t1 = threading.Thread(target=make_window)
    t1.start()

main()