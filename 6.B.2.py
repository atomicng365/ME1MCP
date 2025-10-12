import numpy
import matplotlib.pyplot as plt

N = 2


def facto(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * facto(n - 1)


def Y(x, n):
    if n > 0:
        return x**n / facto(n) + Y(x, n - 1)
    elif n == 0:
        return 1

def ExpSeries(a,dx,b):
    largea = int(a*100)
    largeb = int(b*100)
    largedx = int(dx*100)
    arr = []
    for i in range(largea, largeb+1, largedx):
        arr = arr + [Y(i/100, N)]
    return arr


def ExpSeriesx(a,dx,b):
    largea = int(a*100)
    largeb = int(b*100)
    largedx = int(dx*100)
    arr = []
    for i in range(largea, largeb+1, largedx):
        arr = arr + [i/100]
    return arr

plt.plot(ExpSeriesx(-4, 0.01, 2), ExpSeries(-4, 0.01, 2))

plt.show()
