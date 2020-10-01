import numpy as np
import time


def ComputeBaryW(t):
    n = len(t)
    W = np.ones(n)

    for i in range(n):
        for j in range(n):
            if i is not j:
                W[i] = W[i] / (t[i] - t[j])

    return W


def BaryCentric(x, t, P, W):

    n = P.shape[1]
    N = np.zeros(2)
    D = 0

    for i in range(n):
        if t[i] == x:
            return P[:, i]
        w = W[i] / (x - t[i])
        N = N + w * P[:, i]
        D = D + w

    res = N / D

    return res

def computeBaryCentricePoly(m, n, s, t, P, R, algo_name):

    start = time.time()

    W = ComputeBaryW(t)
    for i in range(m):
        q = BaryCentric(s[i], t, P, W)
        R[:, i] = q

    end = time.time()
    print("Runtime for P{}, algorithm - {}, is {} seconds".format(n, algo_name, end - start))

    return R