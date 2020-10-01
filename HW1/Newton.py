


import numpy as np
import matplotlib.pyplot as plt


eps = 0.000001

def CalcF(s, d, t, x, plotting = False):


    # f(x) = sum (d_i / (s_i + x)) - t

    n = len(s)
    f = 0

    for i in range(n):
        tmp = s[i] + x
        if (tmp == 0) and (not plotting):
             tmp = tmp + eps

        f = f + (d[i] / tmp)

    f = f - t

    return f


def CalcdF(s, d, x):

    # f'(x) = - sum (d_i / (s_i + x)^2)

    n = len(s)
    df = 0

    for i in range(n):
        tmp = s[i] + x
        if tmp == 0:
            tmp = tmp + eps

        df = df - (d[i] / (tmp**2))

    return df

def CalcNewton(s, d, t, x0, max_iter=20):

    x = x0

    for i in range(max_iter):


        f = CalcF(s, d, t, x)
        df = CalcdF(s, d, x)

        print("x_{} is {}, f(x_{}) is {}".format(i, x, i, f))

        e = - f/df
        x = x + e

        if np.fabs(e) < eps:
            break

    return x




def PlotF(s, d, t):

    c = np.linspace(-10, 10, 201)
    f = []

    for i in range(len(c)):
        p = CalcF(s, d, t, c[i], plotting=True)
        f.append(p)

    fig, ax = plt.subplots()
    ax.plot(c, f)
    plt.xticks(np.linspace(-10, 10, 21), (np.linspace(-10, 10, 21)).astype('int16'))

    ax.set(xlabel='x', ylabel='f(x)',
           title='Endless Suffering')

    ax.grid()

    fig.savefig("PlotFc.png")
    plt.show()




def main():

    n = 4
    t = 10
    d = [5, 2, 3, 3]
    s = [3, 2, 6, 1]

    #PlotF(s, d, t)

    c = CalcNewton(s, d, t, -0.9, max_iter=20)
    print("the root c is {}".format(c))



if __name__ == '__main__':
    main()



