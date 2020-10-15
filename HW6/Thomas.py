import numpy as np


eps = 10 ** (-6)

def Thomas(a, b, c, d):

    n = len(d)
    ac, bc, cc, dc = map(np.array, (a, b, c, d))
    for i in range(1, n):
        # if bc[i - 1] == 0:
        #     bc[i - 1] += eps
        mc = ac[i -1] /bc[i - 1]
        bc[i] = bc[i] - mc * cc[i - 1]
        dc[i] = dc[i] - mc * dc[i - 1]

    xc = bc
    xc[-1] = dc[-1] /  bc[-1]

    for i in range(n - 2, -1, -1):
        xc[i] = (dc[i] - cc[i] * xc[i + 1]) / bc[i]

    return xc


def TestThomas():
    A = np.array([[1, 2, 0, 0], [2, 1, 2, 0], [0, 2, 1, 2], [0, 0, 2, 1]], dtype=float)

    a = np.array([2., 2., 2.])
    b = np.array([1., 1., 1., 1.])
    c = np.array([2., 2., 2.])
    d = np.array([1., 2., 3., 4.])

    print("Test results:")
    print(Thomas(a, b, c, d))
    print(np.linalg.solve(A, d))