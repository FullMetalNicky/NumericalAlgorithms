

import numpy as np
import matplotlib.pyplot as plt




def main():


    a = 1
    b = 2

    R = np.zeros((6, 6))




    for j in range(1, 6):

        h_j = (b-a) / (2**(j-1))

        for i in range(1, 2**(j-1) + 1):
            R[j, 1] += np.exp(a + (i - 0.5) * h_j)

        R[j, 1] *= h_j

    for k in range(2, 6):
        for j in range(k, 6):
            R[j, k] = (4**(k-1) * R[j, k - 1] - R[j - 1, k - 1] ) / (4**(k-1) - 1 )


    R = R[1:, 1:]

    print("The modified Romberg integration:")
    print(R)
    print("The accurate result of the integral: {}".format(np.exp(2) - np.exp(1)))


if __name__ == '__main__':
    main()
