import numpy as np
import matplotlib.pyplot as plt
import time
from Neville import computeNevillePoly
from BaryCentric import computeBaryCentricePoly
from NewtonPoly import computeNewtonPoly


def PlotResult(f, R10, R20, R40, algo):

    fig, ax = plt.subplots()
    min_x = np.min(f[0])
    max_x = np.max(f[0])
    ax.set_xlim([min_x-1, max_x+1])
    min_y = np.min(f[1])
    max_y = np.max(f[1])
    ax.set_ylim([min_y-1, max_y+1])

    ax.plot(R10[0], R10[1], color='g', label='P10', alpha=0.5)
    ax.plot(R20[0], R20[1], color='r', label='P20', alpha=0.5)
    ax.plot(R40[0], R40[1], color='b', label='P40', alpha=0.5)
    ax.plot(f[0], f[1], c='k', label='f', alpha=0.5)

    title = "Polynmial interpolatioin in {} algorithm".format(algo)
    plt.title(title)
    ax.grid(True)
    plt.legend()
    plt.savefig(algo+".png")

    plt.show()


def computeF(t):

    coeff = (25*(t**2) + 2) / (25*(t**2) + 1)
    vec = np.array([np.sin(0.5 * np.pi * t), np.cos(0.5 * np.pi * t)])
    f = coeff * vec
    return f

def getData(n,m):

    t = (2 * np.arange(0, n + 1, 1)) / n - 1
    P = computeF(t)
    R = np.zeros((2, m))

    return t, P, R


def main():
    m = 10000
    s = (2 * np.arange(0, m + 1, 1)) / m - 1
    f = computeF(s)

    t10, P10, R10 = getData(10, m)
    t20, P20, R20 = getData(20, m)
    t40, P40, R40 = getData(40, m)

    algo_name = "Neville"
    R10 = computeNevillePoly(m, 10, s, t10, P10, R10, algo_name)
    R20 = computeNevillePoly(m, 20, s, t20, P20, R20, algo_name)
    R40 = computeNevillePoly(m, 40, s, t40, P40, R40, algo_name)
    PlotResult(f, R10, R20, R40, algo_name)

    t10, P10, R10 = getData(10, m)
    t20, P20, R20 = getData(20, m)
    t40, P40, R40 = getData(40, m)

    algo_name = "Barycenteric"
    R10 = computeBaryCentricePoly(m, 10, s, t10, P10, R10, algo_name)
    R20 = computeBaryCentricePoly(m, 20, s, t20, P20, R20, algo_name)
    R40 = computeBaryCentricePoly(m, 40, s, t40, P40, R40, algo_name)
    PlotResult(f, R10, R20, R40, algo_name)

    t10, P10, R10 = getData(10, m)
    t20, P20, R20 = getData(20, m)
    t40, P40, R40 = getData(40, m)

    algo_name = "Newton"
    R10 = computeNewtonPoly(m, 10, s, t10, R10, P10, algo_name)
    R20 = computeNewtonPoly(m, 20, s, t20, R20, P20, algo_name)
    R40 = computeNewtonPoly(m, 40, s, t40, R40,P40, algo_name)
    PlotResult(f, R10, R20, R40, algo_name)






if __name__ == '__main__':
    main()
