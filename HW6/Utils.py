import numpy as np
import matplotlib.pyplot as plt



def Plot(f):

    fig, ax = plt.subplots()
    ax.plot(f[0], f[1], c='k', label='f', alpha=0.5)
    ax.grid(True)
    plt.legend()

    plt.show()


def computeF(t):

    coeff = (25*(t**2) + 2) / (25*(t**2) + 1)
    vec = np.array([np.sin(0.5 * np.pi * t), np.cos(0.5 * np.pi * t)])
    f = coeff * vec
    return f


def getData(n):


    s = (2 * np.arange(0, n + 1, 1)) / n - 1
    P = computeF(s)

    return s, P
