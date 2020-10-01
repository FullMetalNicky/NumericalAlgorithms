import numpy as np
import time


def Neville(x, t, P):

    n = P.shape[1]
    Q = np.zeros(P.shape)

    for i in range(n):
        Q[:, i] = P[:, i]

    for j in range(1,n, 1):
        for i in range(n-j):
            Q_i = Q[:, i]
            Q_next =  Q[:, i + 1]
            Q_i = ((t[i+j] - x) * Q_i + (x - t[i]) * Q_next) / (t[i+j] - t[i])
            Q[:, i] = Q_i

    return Q[:, 0]



def computeNevillePoly(m, n, s, t, P, R, algo_name):

    start = time.time()
    for i in range(m):
        q = Neville(s[i], t, P)
        R[:, i] = q

    end = time.time()
    print("Runtime for P{}, algorithm - {}, is {} seconds".format(n, algo_name, end - start))

    return R