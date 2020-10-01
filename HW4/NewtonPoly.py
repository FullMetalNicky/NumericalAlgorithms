

import numpy as np
import time


def ComputeNewtonB(t, P):

    n = len(t)
    B = np.zeros(P.shape)

    for i in range(n):
        B[:, i] = P[:, i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            B[:, i] = (B[:, i] - B[:, i - 1]) / (t[i] - t[i - j])

    return B

def NewtonPoly(x, t, B):

    n = len(t) - 1
    Q = B[:, n]

    for i in range(n-1, -1, -1):
        Q = Q * (x - t[i]) + B[:, i]

    return Q



def computeNewtonPoly(m, n, s, t, R, P, algo_name):

    start = time.time()

    B = ComputeNewtonB(t, P)
    for i in range(m):
        q = NewtonPoly(s[i], t, B)
        R[:, i] = q

    end = time.time()
    print("Runtime for P{}, algorithm - {}, is {} seconds".format(n, algo_name, end - start))

    return R