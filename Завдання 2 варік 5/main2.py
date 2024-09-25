import threading
import time
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk


class Task:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('task2')
        self.smooth = 100
        self.x_points = [1, 3, 6]
        self.y_points = [3, 5, 3]
        self.coefficients = self.get_the_coefficients()
        self.scatter_color = "red"
        self.line_color = "#00ffff"
        print(self.coefficients)

        self.t = threading.Thread(target=self.create_input_window)
        self.t.start()
        self.x, self.y = self.get_splines(self.x_points, self.coefficients, self.smooth)

        self.scat = self.ax.scatter(self.x_points, self.y_points, color=self.scatter_color)
        self.line, = self.ax.plot(self.x, self.y, color=self.line_color)

        self.ax.grid(True)
        plt.show()

    def F(self, a, b, c, d, x, x0):
        return a + b * (x - x0) + c * (x - x0) ** 2 + d * (x - x0) ** 3

    def get_the_coefficients(self):
        n = (len(self.x_points) - 1) * 4
        matrix_A = np.zeros(shape=[n, n])
        vector_B = np.zeros(shape=n)
        x_points_diff = np.diff(self.x_points)

        for i in range(len(x_points_diff)):
            matrix_A[i * 2][i * 4] = 1
            vector_B[i * 2] = self.y_points[i]
            for j in range(4):
                matrix_A[i * 2 + 1][i * 4 + j] = x_points_diff[i] ** j
                vector_B[i * 2 + 1] = self.y_points[i + 1]

        index = len(x_points_diff) * 2
        for i in range(len(x_points_diff) - 1):
            for j in range(1, 4):
                matrix_A[index][i * 4 + j] = j * x_points_diff[i] ** (j - 1)
            matrix_A[index][i * 4 + 5] = -1
            index += 1
            matrix_A[index][i * 4 + 2] = 2
            matrix_A[index][i * 4 + 3] = 6 * x_points_diff[i]
            matrix_A[index][i * 4 + 6] = -2
            index += 1

        matrix_A[index][2] = 2
        index += 1
        matrix_A[index][-2] = 2
        matrix_A[index][-1] = 6 * x_points_diff[-1]
        print(f"{'=' * 5}Matrix{'=' * 5}\n{matrix_A}\n{'=' * 5}Vector{'=' * 5}\n{vector_B}")
        return np.linalg.solve(matrix_A, vector_B)

    def get_splines(self, x_points, coefficients, smooth):
        x_full = []
        y_full = []
        for i in range(len(x_points) - 1):
            long = x_points[i + 1] - x_points[i]
            x = np.linspace(x_points[i], x_points[i + 1], int(smooth * long))
            a, b, c, d = coefficients[(i * 4): ((i + 1) * 4)]
            y = self.F(a, b, c, d, x, np.array(x_points[i]))
            x_full += list(x)
            y_full += list(y)
        return x_full, y_full

    def button_click(self, delete=False):
        x = float(self.input_x.get())
        if delete:
            if len(self.x_points) == 2:
                self.delete_button['text'] = "Точок не може бути менше ніж 2"
                time.sleep(5)
                self.delete_button['text'] = "Delete"
                return

            y = self.input_y.get()
            if y == "":
                index = self.x_points.index(x)
                self.x_points.remove(x)
                self.y_points.pop(index)
            else:
                y = float(y)
                self.x_points.remove(x)
                self.y_points.remove(y)

        else:
            y = float(self.input_y.get())
            self.x_points.append(x)
            self.x_points.sort()
            self.y_points.insert(self.x_points.index(x), y)


        coefficients = self.get_the_coefficients()
        x_p, y_p = self.get_splines(self.x_points, coefficients, self.smooth)
        self.scat.remove()
        self.scat = self.ax.scatter(self.x_points, self.y_points, color=self.scatter_color)
        self.line.set_data(x_p, y_p)
        self.line.set_color(self.line_color)
        self.fig.canvas.draw()

    def create_input_window(self):
        self.input_window = tk.Tk()
        self.input_window.rowconfigure([0, 1], minsize=1)
        self.input_window.columnconfigure([0, 1, 2, 3], minsize=1)
        tk.Label(master=self.input_window, text="x=", width=5).grid(column=0, row=0)
        self.input_x = tk.Entry(master=self.input_window, width=10)
        self.input_x.grid(column=1, row=0)
        tk.Label(master=self.input_window, text="y=", width=5).grid(column=2, row=0)
        self.input_y = tk.Entry(master=self.input_window, width=10)
        self.input_y.grid(column=3, row=0)
        add_button = tk.Button(master=self.input_window, text="Add", width=20, command=lambda: self.button_click(False))
        add_button.grid(column=0, row=1, columnspan=2)
        self.delete_button = tk.Button(master=self.input_window, text="Delete", width=20, command=lambda: self.button_click(True))
        self.delete_button.grid(column=2, row=1, columnspan=2)
        self.input_window.mainloop()


if __name__ == '__main__':
    Task()