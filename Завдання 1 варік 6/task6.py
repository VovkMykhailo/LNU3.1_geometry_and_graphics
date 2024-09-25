import tkinter as tk
import time
from abc import ABC, abstractmethod
from itertools import chain
from threading import Thread


class MainWindow:
    def __init__(self):
        self.autorun = False
        self.border = 25
        self.dots_size = 3
        self.window = tk.Tk()
        self.window.title("Lab1")
        self.window.rowconfigure([0, 1, 2], minsize=50, weight=1)
        self.window.columnconfigure([0, 1, 2], minsize=50, weight=1)
        self.canvas = tk.Canvas(master=self.window, width=450, height=450, bg="green")
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.entry_N = tk.Entry(master=self.window, width=3, bg='#44ff44')
        self.entry_N.grid(column=0, row=1)
        self.entry_N.insert(0, "8")
        self.entry_R = tk.Entry(master=self.window, width=3, bg='#44ff44')
        self.entry_R.grid(column=2, row=1)
        self.entry_R.insert(0, "400")
        self.entry_Max = tk.Entry(master=self.window, width=3, bg='#44ff44')
        self.entry_Max.grid(column=0, row=2, )
        self.entry_Max.insert(0, "50")
        self.entry_interval = tk.Entry(master=self.window, width=3, bg='#44ff44')
        self.entry_interval.grid(column=2, row=2)
        self.entry_interval.insert(0, "0.1")
        self.btn_r = tk.Button(master=self.window, text="Step", command=self.run_one_image, width=5, height=2,
                               bg='#4444ff')
        self.btn_r.grid(column=1, row=1)
        self.btn15 = tk.Button(master=self.window, text="Run", command=self.run, width=5, height=2, bg='#4444ff')
        self.btn15.grid(column=1, row=2)
        self.window.mainloop()

    def step(self):
        self.canvas.delete('all')
        L = int(self.entry_R.get())  # R
        N = int(self.entry_N.get())
        list_fibonacci = fibonacci(N * 4)

        figure = Square(Point(self.border, self.border), L)
        self.canvas.config(width=L + self.border*2, height=L + self.border*2, bg="green")
        self.canvas.create_polygon(*figure.draw_data(), fill='', outline='black')
        points = figure.get_distributed_points(N)

        for i in range(len(points)):
            for j in get_friendly_points(i, len(points), list_fibonacci):
                self.canvas.create_line(points[i].x, points[i].y, points[j].x, points[j].y)
        self.draw_dots(points, self.dots_size)
        Thread(self.canvas.update()).run()

    def draw_dots(self, points, size):
        for i in points:
            x, y = i.x, i.y
            self.canvas.create_oval(x - size, y - size, x + size, y + size, outline='red', fill='red')

    def run_one_image(self):
        self.autorun = False
        self.btn15['text'] = "Run"
        self.step()

    def run(self):
        if self.autorun:
            self.autorun = False
            return
        self.btn15.config(text="Stop", bg="#ff4444")
        self.autorun = True
        for i in range(int(self.entry_N.get()), int(self.entry_Max.get()) + 1):
            start_time = time.time()
            self.entry_N.delete(0, tk.END)
            self.entry_N.insert(0, str(i))
            self.step()
            end_time = time.time()
            try:
                time.sleep(float(self.entry_interval.get()) + start_time - end_time)
            except ValueError:
                pass
            if not self.autorun:
                break
        self.autorun = False
        self.btn15.config(text="Run", bg="#4444ff")


class Figure(ABC):
    @abstractmethod
    def draw_data(self):
        pass


class Square(Figure):
    def __init__(self, start_point, size):
        self.size = size
        self.A = Point(start_point.x, start_point.y + size)
        self.B = Point(start_point.x, start_point.y)
        self.C = Point(start_point.x + size, start_point.y)
        self.D = Point(start_point.x + size, start_point.y + size)

    def draw_data(self):
        return self.A.draw_data(), self.B.draw_data(), self.C.draw_data(), self.D.draw_data()

    def get_distributed_points(self, n_points):
        return Line(self.A, self.B).get_distributed_points(n_points) +\
               Line(self.B, self.C).get_distributed_points(n_points) +\
               Line(self.C, self.D).get_distributed_points(n_points) +\
               Line(self.D, self.A).get_distributed_points(n_points)


class Line(Figure):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw_data(self):
        return self.point1.draw_data(), self.point2.draw_data()

    def get_distributed_points(self, n_points):
        try:
            step_y = (self.point2.y - self.point1.y) / n_points
            step_x = (self.point2.x - self.point1.x) / n_points
        except ZeroDivisionError:
            step_y, step_x = 0, 0
        return [Point(self.point1.x + step_x * i, self.point1.y + step_y * i) for i in range(n_points)]


class Point(Figure):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def draw_data(self):
        return self.x, self.y


def fibonacci(n):
    list_fibonacci = [1, 2]
    while list_fibonacci[-1] <= n:
        list_fibonacci.append(list_fibonacci[-1]+list_fibonacci[-2])
    return list_fibonacci


def get_friendly_points(index, number_of_points, list_fibonacci):
    for i in list_fibonacci:
        yield (index + i) % number_of_points


MainWindow()