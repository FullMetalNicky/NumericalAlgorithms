

import numpy as np
import matplotlib.pyplot as plt


def sinc(x):
    return np.sin(x)/x


def polyDeg2(x):

    return 3 + 2 * x + x**2

def polyDeg3(x):

    return 1 + x**3

def polyDeg4(x):

    return 1 + x**4


def regRule(x1, x2, x3, h, f):

    res = (4.0 / 3.0) * h * (2 * f(x1) - f(x2) + 2 * f(x3))

    return res


def testRulepPrecision():

    a = 0
    b = 1
    m = 4
    h = (b - a) / m

    # test 2nd degree polynomal
    res = regRule(0.25, 0.5, 0.75, h, polyDeg2)
    print("f(x) is a 2nd degree polynomial")
    print("the integral of f(x) computed by hand is {}".format(13.0 / 3.0))
    print("result approximated is {}".format(res))

    # test 3nd degree polynomal
    res = regRule(0.25, 0.5, 0.75, h, polyDeg3)
    print("f(x) is a 3rd degree polynomial")
    print("the integral of f(x) computed by hand is {}".format(5.0 / 4.0))
    print("result approximated is {}".format(res))

    # test 4nd degree polynomal
    res = regRule(0.25, 0.5, 0.75, h, polyDeg4)
    print("f(x) is a 4th degree polynomial")
    print("the integral of f(x) computed by hand is {}".format(6.0 / 5.0))
    print("result approximated is {}".format(res))



def compositeRule(x, a, b, m, f):

    h = (b - a) / m
    n = int(m / 4)

    res = 0

    for i in range(0, n):

        res += 2 * f(x[4*i+1]) - f(x[4*i + 2]) + 2 * f(x[4*i + 3])

    res = (4.0/3.0)*h * res

    return res



def main():

    testRulepPrecision()

    a = 0
    b = 1
    m = 100
    x = np.linspace(a, b, m + 1)

    res = compositeRule(x, a, b, m, sinc)
    print("the integral of sinx/x computed with wolframalpha is 0.946083")
    print("result approximated with {} segments is {}".format(m, res))
    # app = regRule(0.25, 0.5, 0.75, 0.25, sinc)
    # print(res - app)

if __name__ == '__main__':
    main()
