import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from collections import namedtuple

import keyboard
Point = namedtuple("Point", ['x', 'y'])


def task(Point1, Point2):
    global ax
    X1 = Point1.x
    Y1 = Point1.y
    X2 = Point2.x
    Y2 = Point2.y
    A = Y2 - Y1
    B = X1 - X2
    SingA = -1 if A < 0 else 1
    SingB = -1 if B < 0 else 1
    f = 0
    x = X1
    y = Y1
    pixels.append(Rectangle((x,y),1,1,edgecolor = 'pink',facecolor ='red'))
    if abs(A) < abs(B):
        while True:
            f = f + A*SingA
            if f>0:
                f = f-B*SingB
                y = y + SingA
            x = x - SingB
            pixels.append(Rectangle((x,y),1,1,edgecolor = 'pink',facecolor ='red'))
            if x == X2 and y == Y2:
                break
    else:
        while True:
            f = f+B*SingB
            if f>0:
                f = f - A*SingA
                x = x - SingB
            y = y + SingA
            pixels.append(Rectangle((x,y),1,1,edgecolor = 'pink',facecolor ='red'))
            if x == X2 and y == Y2:
                break


def draw_sun(center):
    global pixels, ax
    start_point = center
    end_point = Point(start_point[0]+32, start_point[1]+32)
    task(start_point, end_point)
    end_point = Point(start_point[0] +32, start_point[1]+16)
    task(start_point, end_point)
    end_point = Point(start_point[0] + 32, start_point[1]+0)
    task(start_point, end_point)
    end_point = Point(start_point[0] + 32, start_point[1]-16)
    task(start_point, end_point)
    end_point = Point(start_point[0] + 32, start_point[1]-32)
    task(start_point, end_point)
    end_point = Point(start_point[0] - 32, start_point[1]-32)
    task(start_point, end_point)
    end_point = Point(start_point[0] - 32, start_point[1]-16)
    task(start_point, end_point)
    end_point = Point(start_point[0] - 32, start_point[1]-0)
    task(start_point, end_point)
    end_point = Point(start_point[0] - 32, start_point[1]+16)
    task(start_point, end_point)
    end_point = Point(start_point[0] - 32, start_point[1]+32)
    task(start_point, end_point)
    end_point = Point(start_point[0] + 16, start_point[1]+32)
    task(start_point, end_point)
    end_point = Point(start_point[0] + 0, start_point[1]+32)
    task(start_point, end_point)
    end_point = Point(start_point[0] - 16, start_point[1]+32)
    task(start_point, end_point)
    end_point = Point(start_point[0] - 16, start_point[1]-32)
    task(start_point, end_point)
    end_point = Point(start_point[0] - 0, start_point[1]-32)
    task(start_point, end_point)
    end_point = Point(start_point[0] + 16, start_point[1]-32)
    task(start_point, end_point)
    draw()

def draw():
    global ax
    for i in pixels:
        ax.add_patch(i)


if __name__ == "__main__":
    pixels = []
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    plt.plot([0, 0], [32, 32])
    plt.xlim([0, 32])
    plt.ylim([0, 32])
    for i in range(33):
        plt.axvline(x=i, ymin=0, ymax=1, linestyle="-", color="black")
    for i in range(33):
        plt.axhline(y=i, xmin=0, xmax=1, linestyle="-", color="black")

    start_point = Point(0, 0)
    end_point = Point(4,7)

    task(start_point, end_point)
    draw()


    def onclick(event):
        global fig, ax, pixels, start_point, end_point

        if keyboard.is_pressed('m'):
            start_point = Point(int(event.xdata), int(event.ydata))
        elif keyboard.is_pressed('n'):
            end_point = Point(int(event.xdata), int(event.ydata))
        elif keyboard.is_pressed('d'):
            task(start_point, end_point)
            draw()
        elif keyboard.is_pressed('c'):
            for p in pixels:
                p.remove()
            pixels.clear()
        elif keyboard.is_pressed('b'):
            point = Point(int(event.xdata), int(event.ydata))
            draw_sun(point)

        fig.canvas.draw()
        print(event)


    cid = fig.canvas.mpl_connect('button_press_event', onclick)

    plt.show()