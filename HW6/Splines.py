
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from Thomas import Thomas
from Thomas import TestThomas
from Utils import *

def deBoor(x, t, D, n):

    k = 0
    E = [0, 0] * n

    while t[n+k+1] < x:
        k += 1

    for i in range(0, n):
        E[:, i] = D[:, i]

    for j in range(1, n):
        for i in range(0, n-j):
            E_i = E[:, i]
            E_next = E[:, i + 1]
            E_i = (E_i * (t[n + i + k + 1] - x) + E_next * (x - t[i + k + j])) / (t[n + i + k + 1] - t[i + k + j])
            E[:, i] = E_i

    return E[:, 0]


def ComputeN(x, t, m, n=3):

    N = np.zeros(2*n+m+1)
    g = len(t)

    for s in range(0, 2*n+m+1):
        if (x >= t[s]) and (x < t[s] + 1):
            N[s] = 1

    for j in range(1, n + 1):
        for i in range(0, 2*n + m - j + 1):
            try:
                N[i] = (x - t[i]) / (t[i +j] - t[i]) * N[i] + (t[i+j+1] - x) / (t[i+j+1] - t[i+1]) * N[i+1]
            except:
                #print("I know..")
                continue

    return N


def ConstructM(t, m):

    M = np.zeros((m + 4, m + 4))

    # boundary conditions
    M[0, 0] = 6
    M[0, 1] = -9
    M[0, 2] = 3

    for i in range(0, m+3):
        N = ComputeN(t[i+3], t, m, 3)
        M[i+1] = N[:m+4]

    M[m+3, m+1] = 3
    M[m+3, m+2] = -9
    M[m+3, m+3] = 6

    return M

def ComputeD(M, P, m):

    px = np.zeros(m+4)
    px[1:-1] = P[0]
    px = px.astype(float32)
    py = np.zeros(m + 4)
    py[1:-1] = P[1]
    py = py.astype(float32)

    M[12, 13] = 1.0
    M[11, 13] = 0.0
    M[11, 12] = 0.25
    M[11, 11] = 7.0 / 12.0

    a = M[:-1, 1:].diagonal().astype(float32)
    b = M.diagonal().astype(float32)
    c = M[1:, :-1].diagonal().astype(float32)

    Dx = np.linalg.solve(M, px)

    Dx2 = Thomas(a, b, c, px)
    Dy = Thomas(a, b, c, py)

    return Dx, Dy


def TestN(t, m):

    p = []
    v = []
    for x in arange(5, 9, 0.1):
        N = ComputeN(x, t, m, 3)
        val = N[8]
        p.append(val)
        v.append(x)

    p2 = []
    v2 = []
    for x in arange(6, 10, 0.1):
        N = ComputeN(x, t, m, 3)
        val = N[9]
        p2.append(val)
        v2.append(x)

    p3 = []
    v3 = []
    p4 = []
    for x in arange(7, 11, 0.1):
        N = ComputeN(x, t, m, 3)
        val = N[10]
        p3.append(val)
        v3.append(x)
        p4.append(N[11])

    fig, ax = plt.subplots()
    ax.plot(v, p, c='k', alpha=0.5)
    ax.plot(v2, p2, c='g', alpha=0.5)
    ax.plot(v3, p3, c='b', alpha=0.5)
    ax.plot(v3, p4, c='r', alpha=0.5)

    ax.grid(True)
    plt.legend()
    plt.show()


def main():
    m = 10
    n = 100

    # Generate interpolation points P
    s, P = getData(m+1)
    #Utils.Plot(P)

    # Create knots
    t = list(range(-3, m + 5))
    t[0] = t[1] = t[2] = t[3] = 0
    t[m + 4] = t[m + 5] = t[m + 6] = t[m + 7] = m + 1

    #Compute matrix M
    M = ConstructM(t, m)
    #TestN(t, m)

    # compute deBoor coefficients
    Dx, Dy = ComputeD(M, P, m)

    Ecurve = []
    for x in arange(4, 10, 0.1):
        E = deBoor(x, t, Dx, 3)
        Ecurve.append(E)

    #TestThomas()











if __name__ == '__main__':
    main()