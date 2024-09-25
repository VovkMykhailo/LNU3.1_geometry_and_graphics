import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import simpledialog


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def findC(t, points):
    pointC = Point(0, 0)
    matrix = [[-1, 3, -3, 1],
              [2, -5, 4, -1],
              [-1, 0, 1, 0],
              [0, 2, 0, 0]]
    vector = [t * t * t, t * t, t, 1]

    vectorTA = [0, 0, 0, 0]
    i = 0
    while (i < 4):
        j = 0
        while (j < 4):
            vectorTA[i] += vector[j] * matrix[j][i]
            j += 1
        i += 1

    for k in range(4):
        pointC.x += vectorTA[k] * points[k].x
    for k in range(4):
        pointC.y += vectorTA[k] * points[k].y

    pointC.x = pointC.x * 0.5
    pointC.y = pointC.y * 0.5

    return pointC


def drawInterpolatedParabola(p1, p2, p3, p4):
    point1 = findC(0, [p1, p2, p3, p4])
    point2 = point1

    t = 0
    while t < 1:
        point1 = point2
        point2 = findC(t, [p1, p2, p3, p4])
        plt.plot(point1.x, point1.y, point2.x, point2.y, marker="o", ms=1, color="black")
        # plt.pause(0.001)
        t += 0.01


def drawParabola(x1_array, x2_array, y1_array, y2_array):
    plt.xlim(x1_array[0], x1_array[len(x1_array) - 1])
    plt.ylim(min(y1_array) - 5, max(y1_array) + 5)

    x1Array = np.arange(x1_array[0], x1_array[2], step).tolist()
    x2Array = np.arange(x2_array[0], x2_array[2], step).tolist()

    for i in range(len(x1Array)):
        if i == len(x1Array) - 1:
            break

        tempX = [x1Array[i], x1Array[i + 1]]
        tempY = [y1_array[i], y1_array[i + 1]]
        plt.plot(tempX, tempY, color="blue")
        plt.pause(0.001)

    for i in range(len(x2Array)):
        if i == len(x2Array) - 1:
            break

        tempX = [x2Array[i], x2Array[i + 1]]
        tempY = [y2_array[i], y2_array[i + 1]]
        plt.plot(tempX, tempY, color="red")
        plt.pause(0.001)


# finds Y for parabola
def findInterpolatedY(xArray, yArray, x):
    result = 0
    index1, index2 = 1, 2

    for i in range(3):
        result += yArray[i] * ((x - xArray[index1]) * (x - xArray[index2])
                               / ((xArray[i] - xArray[index1]) * (xArray[i] - xArray[index2])))

        index1 += 1
        index2 += 1
        if (index1 % 3) == 0:
            index1 = 0
        if (index2 % 3) == 0:
            index2 = 0

    return result


if __name__ == '__main__':
    ROOT = tk.Tk()
    ROOT.withdraw()
    point1x = simpledialog.askinteger(title="Geometry",
                                      prompt="Enter x of point 1:")
    point1y = simpledialog.askinteger(title="Geometry",
                                      prompt="Enter y of point 1:")
    point2x = simpledialog.askinteger(title="Geometry",
                                      prompt="Enter x of point 2:")
    point2y = simpledialog.askinteger(title="Geometry",
                                      prompt="Enter y of point 2:")
    point3x = simpledialog.askinteger(title="Geometry",
                                      prompt="Enter x of point 3:")
    point3y = simpledialog.askinteger(title="Geometry",
                                      prompt="Enter y of point 3:")
    point4x = simpledialog.askinteger(title="Geometry",
                                      prompt="Enter x of point 4:")
    point4y = simpledialog.askinteger(title="Geometry",
                                      prompt="Enter y of point 4:")

    p1 = Point(point1x, point1y)
    p2 = Point(point2x, point2y)
    p3 = Point(point3x, point3y)
    p4 = Point(point4x, point4y)

    x1Array = [p1.x, p2.x, p3.x]
    y1Array = [p1.y, p2.y, p3.y]
    x2Array = [p2.x, p3.x, p4.x]
    y2Array = [p2.y, p3.y, p4.y]

    interpolatedArray1 = []
    interpolatedArray2 = []
    i = x1Array[0]
    step = 0.1
    n = x1Array[2]
    while i < n:
        interpolatedArray1.append(findInterpolatedY(x1Array, y1Array, i))
        i += step

    i = x2Array[0]
    n = x2Array[2]
    while i < n:
        interpolatedArray2.append(findInterpolatedY(x2Array, y2Array, i))
        i += step

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    drawParabola(x1Array, x2Array, interpolatedArray1, interpolatedArray2)
    drawInterpolatedParabola(p1, p2, p3, p4)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()