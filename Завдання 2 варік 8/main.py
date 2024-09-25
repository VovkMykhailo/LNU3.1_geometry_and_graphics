from spline import build_cubic_splines, build_acyclic_splines
import numpy as np

if __name__ == '__main__':
    #P = np.array([[0, 0, 0], [3, 3, 3], [2, 4, 3], [2, 3, 1], [5, 4, 6], [4, 8, 2], [0, 0, 0]])
    P = np.array([[0, 0, 0], [3, 3, 3], [2, 2, 2], [-3, -3, 3], [0, 0, 0]])
    P_1_dash = [0.3, 0.3, 0.3]
    P_2_dash = [0.7, 0.7, 0.7]

    build_cubic_splines(P, P_1_dash, P_2_dash)
    build_acyclic_splines(P)