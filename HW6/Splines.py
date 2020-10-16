
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
from Thomas import Thomas
from Thomas import TestThomas
from Utils import *
from matplotlib.pyplot import cm


def deBoor(x, t, D, m, n=3):

    F = np.array([0, 0]).astype(float64)

    N = ComputeN(x, t, m, n)

    for i in range(m+n+1):
        F += D[:, i] * N[i]

    return F


def ComputeN(x, t, m, n=3):

    N = np.zeros(2*n + m +1)

    for s in range(0, 2*n + m +1):
        if (x >= t[s]) and (x < t[s + 1]):
            N[s] = 1

    if x >= t[m+n+1]:
        N[m+n]= 1

    for j in range(1, n + 1):
        for i in range(0, 2*n + m +1 - j):
            if (t[i +j] - t[i]) > 0:
                N[i] = (x - t[i]) / (t[i + j] - t[i]) * N[i]
            else:
                N[i] = 0
            if (t[i+j+1] - t[i+1]) > 0:
                N[i] += (t[i+j+1] - x) / (t[i+j+1] - t[i+1]) * N[i+1]

    return N


def ConstructM(t, m):

    M = np.zeros((m + 4, m + 4))

    # boundary conditions
    M[0, 0] = 6
    M[0, 1] = -9
    M[0, 2] = 3

    for i in range(0, m+2):
        N = ComputeN(t[i+3], t, m, 3)
        M[i+1] = N[:m+4]

    M[m+3, m+1] = 3
    M[m+3, m+2] = -9
    M[m+3, m+3] = 6

    # swap rows to make it tridiagonal
    M[[0,1]] = M[[1,0]]
    M[[m+3, m+2]] = M[[m+2, m+3]]

    return M

def ComputeD(M, P, m):

    px = np.zeros(m+4)
    px[1:-1] = P[0]
    px[0], px[1] = px[1], px[0]
    px[m+3], px[m+2] = px[m+2], px[m+3]
    px = px.astype(float32)

    py = np.zeros(m + 4)
    py[1:-1] = P[1]
    py[0], py[1] = py[1], py[0]
    py[m+3], py[m +2] = py[m+3], py[m+3]
    py = py.astype(float32)

    np.set_printoptions(precision=2)
    np.set_printoptions(suppress=True)

    print('Matrix M is ')
    for row in M:
        for col in row:
            print("{0:0.3f}".format(col), end =" ")
        print()
    print("Interpolation points are: ")
    print(px)
    print(py)
    print('Solving MD=P: ')

    # subdiagonal
    a = M[1:, :-1].diagonal().astype(float32)
    # diagonal
    b = M.diagonal().astype(float32)
    # super-diagonal
    c = M[:-1, 1:].diagonal().astype(float32)

    Dx = Thomas(a, b, c, px)
    Dy = Thomas(a, b, c, py)

    print('Dx is {}'.format(Dx))
    print('Dy is {}'.format(Dy))

    return Dx, Dy


def TestPlotN(t, m):

    p = np.zeros((m+4, 130))
    v = []

    j = 0
    for x in arange(0, m+4, 0.1):
        N = ComputeN(x, t, m, 3)
        v.append(x)
        for i in range(m+4):
            p[i, j] = N[i]

        j += 1

    color = iter(cm.rainbow(np.linspace(0, 1, m+4)))

    fig, ax = plt.subplots()
    for i in range(m+4):
        c = next(color)
        ax.plot(v, p[i], c=c, alpha=0.5)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.grid(True)
    plt.title("Basis functions of degree 3")
    #plt.legend()
    plt.savefig("N3.png")
    plt.show()


def Suffer(m):
    # Generate interpolation points P
    s, P = getData(m + 1)
    # Utils.Plot(P)

    # Create knots
    t = list(range(-3, m + 5))
    t[0] = t[1] = t[2] = t[3] = 0
    t[m + 4] = t[m + 5] = t[m + 6] = t[m + 7] = m + 1

    # Compute matrix M
    M = ConstructM(t, m)
    # TestPlotN(t, m)

    # compute deBoor coefficients
    # TestThomas()
    Dx, Dy = ComputeD(M, P, m)
    D = np.vstack((Dx, Dy))
    D = np.asarray(D)


    i = 0
    params = arange(t[3], t[m + 4] + 0.1, 0.1)
    l = len(params)
    Ecurve = np.zeros((2, l))
    s = (2 * np.arange(0, l + 1, 1)) / l - 1

    # compute the P function of last exrecise
    f = computeF(s)

    # reconstruct the curve
    for x in params:
        E = deBoor(x, t, D, m, 3)
        Ecurve[:, i] = E
        i += 1

    Plot(Ecurve, f, m + 1)


def main():


    Suffer(m=9)

    Suffer(m=19)

    Suffer(m=39)













if __name__ == '__main__':
    main()