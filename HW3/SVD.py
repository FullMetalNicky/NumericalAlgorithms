import numpy as np
import matplotlib.pyplot as plt


def ComputeBaryCenters(x):

    x_mean = np.mean(x, axis=1)

    return x_mean

def ComputeEigenvalus(A):
    a = A[0][0]
    b = A[0][1]
    c = A[1][1]

    tmp = np.sqrt((a - c)**2 + 4*(b**2))

    lambda1 = ((a + c) + tmp) / 2
    lambda2 = ((a + c) - tmp) / 2

    return lambda1, lambda2

def ComputeEigenvector(A, lamb):
    b = A[0][1]
    c = A[1][1]

    v = np.array([lamb - c, b])
    v = v / np.linalg.norm(v)

    return v

def PlotPoints(P, Q):
    fig, ax = plt.subplots()
    ax.scatter(Q[0], Q[1], c='b', label='Q')
    ax.scatter(P[0], P[1], c='g', label='P')

    ax.grid()
    plt.legend()

    fig.savefig("SVD.png")
    plt.show()

def PlotPointsFinal(P, Q, Q_trans):
    fig, ax = plt.subplots()
    ax.scatter(P[0], P[1], c='g', label='P')
    ax.scatter(Q[0], Q[1], c='b', label='Q')
    ax.scatter(Q_trans[0], Q_trans[1], c='r', label='Q_trans')

    ax.grid()
    plt.legend()
    plt.title("Point Matching with IPC")

    fig.savefig("SVDRes.png")
    plt.show()

def CalcTransformedPoints(Q, R, t):
    Q_trans = np.zeros(Q.shape)
    for i in range(Q.shape[1]):
        tmp = R @ Q[:, i]
        Q_trans[:, i] = tmp + t


    return Q_trans

def CalcError(P, Q_trans):

    dist = P-Q_trans
    error = 0
    for i in range(P.shape[1]):
        error = error + dist[0, i]**2 + dist[1, i]**2

    return error


def FixVIfReflection(V):

    if V[0][1] * V[1][0] < 0:
        V[:, 0] = -1 * V[:, 0]

    return V

def FindTransform(P, Q):

    n = P.shape[1]
    P_mean = ComputeBaryCenters(P)
    Q_mean = ComputeBaryCenters(Q)

    P_hat = P - np.array([P_mean, ] * n).transpose()
    Q_hat = Q - np.array([Q_mean, ] * n).transpose()

    A = 0

    for i in range(n):
        A = A + np.outer(P_hat[:, i], Q_hat[:, i].transpose())

    M = A.T @ A
    lambda1, lambda2 = ComputeEigenvalus(M)
    v1 = ComputeEigenvector(M, lambda1)
    v2 = ComputeEigenvector(M, lambda2)
    V = np.array([v1, v2]).T
    V = FixVIfReflection(V)

    M2 = A @ A.T
    lambda1, lambda2 = ComputeEigenvalus(M2)
    u1 = ComputeEigenvector(M2, lambda1)
    u2 = ComputeEigenvector(M2, lambda2)
    U = np.array([u1, u2]).T
    U = FixVIfReflection(U)

    # D = np.diag((np.sqrt(lambda1), np.sqrt(lambda2)))
    # U = A @ np.linalg.inv(D @ V.T)
    #U2, S, V2 = np.linalg.svd(A)

    R = U @ V.T
    t = P_mean - R @ Q_mean

    return R, t

def main():

    P = np.array([[-2.4, 0.5, -3.0, -1.1, -3.6, -0.7], [-1.6, -0.7, 0.3, 0.9, 2.2, 3.1]])
    Q = np.array([[-0.3, 1.6, 1.3, 2.5, 2.8, 4.7], [0.5, -1.8, 1.7, 0.5, 3.0, 0.6]])


    R, t = FindTransform(P, Q)
    print("R is {}".format(R))
    print("t is {}".format(t))

    Q_trans = CalcTransformedPoints(Q, R, t)
    error = CalcError(P, Q_trans)
    print("F(R,t) is {}".format(error))
    print("The new Q is {}".format(Q_trans))

    PlotPointsFinal(P, Q, Q_trans)




if __name__ == '__main__':
    main()
