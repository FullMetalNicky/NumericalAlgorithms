import numpy as np



def Thomas(a, b, c, d):

    n = len(d)
    a_, b_, c_, d_ = map(np.array, (a, b, c, d))
    for i in range(1, n):
        w = a_[i - 1] / b_[i - 1]
        b_[i] = b_[i] - w * c_[i - 1]
        d_[i] = d_[i] - w * d_[i - 1]

    x = b_
    x[-1] = d_[-1] / b_[-1]

    for j in range(n - 2, -1, -1):
        x[j] = (d_[j] - c_[j] * x[j + 1]) / b_[j]

    return x



def TestThomas():
    A = np.array([[1, 2, 0, 0], [2, 3, 2, 0], [0, 2, 1, 2], [0, 0, 3, 1]], dtype=float)

    print("Matrix A = {}".format(A))
    a = np.array([2., 2., 3.])
    b = np.array([1., 3., 1., 1.])
    c = np.array([2., 2., 2])
    d = np.array([1., 2., 3., 4.])
    print("Vector d = {}".format(d))

    print("Solving Ax=d")
    print("Thomas algorithm: {}".format(Thomas(a, b, c, d)))
    print("Numpy solver: {}".format(np.linalg.solve(A, d)))