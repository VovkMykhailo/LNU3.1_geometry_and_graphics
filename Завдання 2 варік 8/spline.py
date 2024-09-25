import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import linalg


class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, k: float):
        return Vector(self.x * k, self.y * k, self.z * k)

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)

    def __repr__(self):
        return "Vector:({0},{1},{2})".format(self.x, self.y, self.z)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getz(self):
        return self.z


def simple_mul(matr1, matr2, n1, m1, m2):
    mulMatr = [[0 for j in range(m2)] for i in range(n1)]
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                mulMatr[i][j] += matr1[i][k] * matr2[k][j]
    return mulMatr

def vector_matr_mul(matr,vect,r):
    res = [Vector(0, 0, 0) for i in range(r)]
    for i in range(r):
        for j in range(r):
            res[i] = res[i] + (vect[j]*matr[i][j])
    return res


def vector_mul(matr1, matr2, n1, m1, m2):
    mulMatr = [[Vector(0, 0, 0) for j in range(m2)] for i in range(n1)]
    for i in range(n1):
        for j in range(m2):
            for k in range(m1):
                mulMatr[i][j] = matr2[k][j] * matr1[i][k] + mulMatr[i][j]
    return mulMatr


def build_cubic_splines(P,P_1_dash, P_n_dash):
    P_vectors = [Vector(*i) for i in P]
    P_1_dash = Vector(*P_1_dash)
    P_n_dash = Vector(*P_n_dash)
    n = P.shape[0]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(P[:, 0], P[:, 1], P[:, 2])

    hord = []

    for i in range(1, n):
        a=np.sqrt((P_vectors[i].getx()-P_vectors[i-1].getx())**2 + (P_vectors[i].gety()-P_vectors[i-1].gety())**2 + (P_vectors[i].getz()-P_vectors[i-1].getz())**2)
        hord.append(a)
    M = np.zeros(shape=(n, n))
    M[0, 0] = 1
    M[0, 1] = 0
    M[n - 1, n - 2] = 0
    M[n - 1, n - 1] = 1

    for i in range(1, n - 1):
        M[i, i - 1] = hord[i]
        M[i, i] = 2*(hord[i]+hord[i-1])
        M[i, i + 1] = hord[i-1]
    eq = [Vector(0,0,0) for i in range(n)]
    eq[0]=P_1_dash
    eq[n-1]=P_n_dash
    for i in range(1, n-1):
        a = ((P_vectors[i+1]-P_vectors[i])*(hord[i-1]**2)+(P_vectors[i]-P_vectors[i-1])*(hord[i]**2))*(3/(hord[i-1]*hord[i]))
        eq[i]=a

    Mt = linalg.inv(M)
    pdash = vector_matr_mul(Mt,eq,n)
    print("---Ordinary---")
    print("PDash:")
    print(pdash)
    b = [[Vector(0, 0, 0) for j in range(4)] for i in range(n)]
    for i in range(n-1):
        b[i][0] = P_vectors[i]
        b[i][1] = pdash[i]
        b[i][2] = ((P_vectors[i+1]-P_vectors[i])*3)*(1/hord[i]**2) - (pdash[i]*2)*(1/hord[i]) - pdash[i+1]*(1/hord[i])
        b[i][3] = ((P_vectors[i]-P_vectors[i+1])*2)*(1/hord[i]**3) + (pdash[i])*(1/hord[i]**2) + pdash[i+1]*(1/(hord[i]**2))

    x = []
    y = []
    z = []
    for i in range(n - 1):
        for t in np.arange(0, hord[i], 0.01):
            a = b[i][0] + b[i][1] * t + b[i][2] * t**2 + b[i][3] * t**3
            x.append(a.getx())
            y.append(a.gety())
            z.append(a.getz())
        #a = Vector([b[i][0] + b[i][1] * t + b[i][2] * t**2 + b[i][3] * t**3 for t in np.arange(0, hord[i], 0.01)])

    ax.plot3D(np.array(x),np.array(y),np.array(z))

def build_acyclic_splines(P):
    P_vectors = [Vector(*i) for i in P]
    n = P.shape[0]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(P[:, 0], P[:, 1], P[:, 2])

    hord = []

    for i in range(1, n):
        a = np.sqrt((P_vectors[i].getx() - P_vectors[i - 1].getx()) ** 2 + (
                    P_vectors[i].gety() - P_vectors[i - 1].gety()) ** 2 + (
                                P_vectors[i].getz() - P_vectors[i - 1].getz()) ** 2)
        hord.append(a)

    M = np.zeros(shape=(n-1, n-1))
    M[0, 0] = 2*(1+hord[n-2]/hord[0])
    M[0, 1] = hord[n-2]/hord[0]
    M[0, n - 2] = -1

    for i in range(1, n - 2):
        M[i, i - 1] = hord[i]
        M[i, i] = 2 * (hord[i] + hord[i - 1])
        M[i, i + 1] = hord[i - 1]

    eq = [Vector(0, 0, 0) for i in range(n)]
    eq[0] = (P_vectors[1]-P_vectors[0])*(hord[n-2]/hord[0]**2)*3 + (P_vectors[n-2]-P_vectors[n-1])*(3/hord[n-2])
    for i in range(1, n - 2):
        a = ((P_vectors[i + 1] - P_vectors[i]) * (hord[i - 1] ** 2) + (P_vectors[i] - P_vectors[i - 1]) * (
                    hord[i] ** 2)) * (3 / (hord[i - 1] * hord[i]))
        eq[i] = a

    Mt = np.linalg.pinv(M)
    pdash = vector_matr_mul(Mt, eq, n-1)

    pdash.append(Vector(-pdash[0].getx(),-pdash[0].gety(),-pdash[0].getz()))

    b = [[Vector(0, 0, 0) for j in range(4)] for i in range(n)]
    for i in range(n - 1):
        b[i][0] = P_vectors[i]
        b[i][1] = pdash[i]
        b[i][2] = ((P_vectors[i + 1] - P_vectors[i]) * 3) * (1 / hord[i] ** 2) - (pdash[i] * 2) * (1 / hord[i]) - pdash[
            i + 1] * (1 / hord[i])
        b[i][3] = ((P_vectors[i] - P_vectors[i + 1]) * 2) * (1 / hord[i] ** 3) + (pdash[i]) * (1 / hord[i] ** 2) + \
                  pdash[i + 1] * (1 / (hord[i] ** 2))

    x = []
    y = []
    z = []
    for i in range(n - 1):
        for t in np.arange(0, hord[i], 0.01):
            a = b[i][0] + b[i][1] * t + b[i][2] * t ** 2 + b[i][3] * t ** 3
            x.append(a.getx())
            y.append(a.gety())
            z.append(a.getz())


    ax.plot3D(np.array(x), np.array(y), np.array(z))


    print("---ACyclic---")
    print("PDash:")
    print(pdash)

    plt.show()

