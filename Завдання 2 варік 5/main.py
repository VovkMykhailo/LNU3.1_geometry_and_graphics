import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
import keyboard


def S_n(a, b, c, d, x, x0):
    return a + b * (x - x0) + c * (x - x0)**2 + d * (x - x0)**3


def get_the_coefficients(x_points, y_points, show=False):
    n = (len(x_points) - 1) * 4

    if len(x_points) != len(y_points):
        raise Exception("Len error :(")

    matrix_A = np.zeros(shape=[n, n])
    vector_B = np.zeros(shape=n)
    x_points_diff = np.diff(x_points)

    for i in range(len(x_points_diff)):
        matrix_A[i*2][i*4] = 1
        vector_B[i*2] = y_points[i]
        for j in range(4):
            matrix_A[i*2 + 1][i*4 + j] = x_points_diff[i]**j
            vector_B[i*2 + 1] = y_points[i + 1]

    index = len(x_points_diff) * 2
    for i in range(len(x_points_diff) - 1):
        matrix_A[index][i*4 + 1] = 1
        matrix_A[index][i*4 + 2] = 2 * x_points_diff[i]
        matrix_A[index][i*4 + 3] = 3 * x_points_diff[i]**2
        matrix_A[index][i*4 + 5] = -1
        index += 1
        matrix_A[index][i*4 + 2] = 2
        matrix_A[index][i*4 + 3] = 6 * x_points_diff[i]
        matrix_A[index][i*4 + 6] = -2
        index += 1

    matrix_A[index][2] = 2
    index += 1
    matrix_A[index][-2] = 2
    matrix_A[index][-1] = 6 * x_points_diff[-1]

    if show == True:
        infowin = tk.Tk()
        infowin.columnconfigure([0, 1], minsize=1)
        df_matrix = round(pd.DataFrame(matrix_A), 2)
        df_vector = round(pd.Series(vector_B), 4)

        label_matrix_a = tk.Label(master=infowin, text=pd.DataFrame(df_matrix).to_string(index=False, header=False), background="#2222ff")
        text_b = "\n".join(list(map(lambda x: str(x), df_vector)))
        print(text_b)
        label_vector_b = tk.Label(master=infowin, text=text_b, background="#444488")
        label_matrix_a.grid(column=0, row=0)
        label_vector_b.grid(column=1, row=0)
        infowin.mainloop()
        return

    return np.linalg.solve(matrix_A, vector_B)


def get_splines(x_points, coefficients, smooth):
    x_full = []
    y_full = []
    for i in range(len(x_points) - 1):
        long = x_points[i + 1] - x_points[i]
        x = np.linspace(x_points[i], x_points[i + 1], int(smooth * long))
        a, b, c, d = coefficients[(i * 4): ((i+1) * 4)]
        y = S_n(a, b, c, d, x, np.array(x_points[i]))
        x_full += list(x)
        y_full += list(y)
    return x_full, y_full


if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.set_title('task2')
    smooth = 100
    x_points = [0, 7, 10]
    y_points = [0, 1, 10]
    coefficients = get_the_coefficients(x_points, y_points)
    x, y = get_splines(x_points, coefficients, smooth)

    scat = ax.scatter(x_points, y_points, color="#4444ff")
    line, = ax.plot(x, y)


    def onclick(event):
        global x_points, y_points, scat

        if keyboard.is_pressed('m'):
            get_the_coefficients(x_points, y_points, True)
        elif keyboard.is_pressed('n'):
            x_points.append(event.xdata)
            x_points.sort()
            y_points.insert(x_points.index(event.xdata), event.ydata)
        elif keyboard.is_pressed('c'):
            x_points = [0, 10]
            y_points = [0, 10]
        coefficients = get_the_coefficients(x_points, y_points)
        x_p, y_p = get_splines(x_points, coefficients, smooth)
        scat.remove()
        scat = ax.scatter(x_points, y_points, color="#4444ff")
        line.set_data(x_p, y_p)
        fig.canvas.draw()

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    ax.grid(True)
    plt.show()