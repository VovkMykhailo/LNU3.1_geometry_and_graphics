import tkinter as tk
import time
autorun = False

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # def __add__(self, other):
    #     return Point(self.x + other.x, self.y + other.y)
    #
    # def __sub__(self, other):
    #     return Point(self.x - other.x, self.y - other.y)

def Fibonacci(n):
    list_fibonacci = [1, 2]
    while list_fibonacci[-1] <= n:
        list_fibonacci.append(list_fibonacci[-1]+list_fibonacci[-2])
    return list_fibonacci

def Get_friendly_points(index, number_of_points, list_fibonacci):
    for i in list_fibonacci:
        yield (index + i)%number_of_points

def Step():
    w.delete('all')
    L = int(entry_R.get()) #R
    N = int(entry_N.get())
    border = 25
    list_fibonacci = Fibonacci(N*4)
    w.config(width=L + border*2, height=L + border*2)
    w.create_rectangle(border, border, L + border, L + border)

    step = L/N
    points = []
    for i in range(N):
        x = border + step*i
        y = border
        points.append(Point(x, y))

    for i in range(N):
        x = border + L
        y = border + step*i
        points.append(Point(x, y))

    for i in range(N):
        x = border + L - step*i
        y = border + L
        points.append(Point(x, y))

    for i in range(N):
        x = border
        y = border + L - step*i
        points.append(Point(x,y))

    for i in range(N*4):
        for j in Get_friendly_points(i, N*4, list_fibonacci):
            x1, y1 = points[i-1].x, points[i-1].y
            x2, y2 = points[j-1].x, points[j-1].y
            w.create_line(x1, y1, x2, y2)

    for i in points:
        x, y = i.x, i.y
        size = 3
        w.create_oval(x - size, y - size, x + size, y + size, outline='red', fill='red')

def Run1():
    global autorun
    autorun = False
    btn15['text'] = "Run"
    Step()

def Run2():
    global autorun
    if autorun:
        autorun = False
        return
    btn15.config(text="Stop", bg="#ff4444")
    autorun = True
    for i in range(int(entry_N.get()), int(entry_Max.get())+1):
        entry_N.delete(0, tk.END)
        entry_N.insert(0, str(i))
        start = time.time()
        Step()
        end = time.time()
        try:
            show_fps = True
            if show_fps:
                btn15['text'] = round(1/(end-start))
        except ZeroDivisionError:
            pass
        window.update()
        try:
            time.sleep(float(entry_interval.get()))
        except:
            pass
        if not autorun:
            break
    btn15.config(text="Run", bg="#4444ff")



window=tk.Tk()
window.title("Lab1")
w=tk.Canvas(width=450,height=450,bg="green")

window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
w.grid(row=0, column=0,columnspan=3)

entry_N=tk.Entry(master=window,width=3, bg='#44ff44')
entry_N.grid(column=0, row=1,)
entry_N.insert(0,"8")
entry_R=tk.Entry(master=window,width=3,bg='#44ff44')
entry_R.grid(column=2, row=1)
entry_R.insert(0,"400")
btn_r = tk.Button(master=window,text="Step",command=Run1,width=5,height=2,bg='#4444ff')
btn_r.grid(column=1, row=1)
entry_Max = tk.Entry(master=window,width=3, bg='#44ff44')
entry_Max.grid(column=0, row=2,)
entry_Max.insert(0,"50")
entry_interval = tk.Entry(master=window,width=3,bg='#44ff44')
entry_interval.grid(column=2, row=2)
entry_interval.insert(0,"0.1")
btn15 = tk.Button(master=window,text="Run",command=Run2,width=5,height=2,bg='#4444ff')
btn15.grid(column=1, row=2)
window.mainloop()
