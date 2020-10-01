
import numpy as np
import matplotlib.pyplot as plt


eps = 10 ** (-16)


def GaussSeidel(d, sub_d, sup_d, anti_d, x, b, n):

    a_ii = d

    for iter in range(1000):
        max_diff = 0.0
        for i in range(n):
            sum = 0

            # We don't have a sub-diag element
            if i == 0:
                sum = sup_d * x[i+1] + anti_d * x[n - 1 - i]
            # The diag element overwrites the anti-diag
            elif i == int(n/2):
                sum = sup_d * x[i + 1] + sub_d * x[i - 1]
            elif i < n - 1:
                sum = sup_d * x[i + 1] + sub_d * x[i - 1] + anti_d * x[n - 1 - i]
            # We don't have a super-diag element
            elif i == (n-1):
                sum = sub_d * x[i - 1] + anti_d * x[n - 1 - i]

            res = (b[i] - sum) / a_ii

            diff = np.fabs(x[i] - res)
            if max_diff < diff:
                max_diff = diff

            x[i] = res

        #print("x_{} is {}".format(iter, x))
        print("iter is {}".format(iter))

        if max_diff < eps:
            break

    return x


def main():

    n = 99999
    x_0 = np.zeros(n)
    d = 6
    sub_d = -2
    sup_d = -2
    anti_d = 1
    b = 3 * np.ones(n)
    b[0] = 5
    b[n-1] = 5
    b[int(n/2)] = 2


    x = GaussSeidel(d, sub_d, sup_d, anti_d, x_0, b, n)
    print("Converged. x is {}".format(x))



if __name__ == '__main__':
    main()
