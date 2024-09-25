import tkinter as tk
from math import sqrt


class MainWindow:
    def __init__(self):
        self.autorun = False
        self.border = 25
        self.dots_size = 3
        self.window = tk.Tk()
        self.canvas = tk.Canvas(master=self.window, width=450, height=450, bg="green")
        self.canvas.pack()
        self.figure_type = [Square, Triangle][1]
        self.N = 5
        self.L = 400
        self.draw()
        self.window.mainloop()

    def draw(self):
        self.canvas.delete('all')
        list_fibonacci = fibonacci(self.N * 4)
        figure = self.figure_type(Point(self.border, self.border), self.L)
        self.canvas.config(width=self.L + self.border*2, height=self.L + self.border*2, bg="green")
        self.canvas.create_polygon(*figure.draw_data(), fill='', outline='black')
        points = figure.get_distributed_points(self.N)

        for i in range(len(points)):
            for j in get_friendly_points(i, len(points), list_fibonacci):
                self.canvas.create_line(points[i].x, points[i].y, points[j].x, points[j].y)
        self.draw_dots(points, self.dots_size)
        self.canvas.update()

    def draw_dots(self, points, size):
        for i in points:
            x, y = i.x, i.y
            self.canvas.create_oval(x - size, y - size, x + size, y + size, outline='red', fill='red')


class Triangle:
    def __init__(self, start_point, size):
        self.size = size
        start_point = Point(start_point.x, start_point.y+size)
        self.A = Point(start_point.x, start_point.y)
        self.B = Point(start_point.x + size/2, start_point.y - size*sqrt(3)/2)
        self.C = Point(start_point.x + size, start_point.y)

    def draw_data(self):
        return self.A.draw_data(), self.B.draw_data(), self.C.draw_data()

    def get_distributed_points(self, n_points):
        return Line(self.A, self.B).get_distributed_points(n_points) +\
               Line(self.B, self.C).get_distributed_points(n_points) +\
               Line(self.C, self.A).get_distributed_points(n_points)


class Square:
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


class Line:
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


class Point:
    def __init__(self, x, y):
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