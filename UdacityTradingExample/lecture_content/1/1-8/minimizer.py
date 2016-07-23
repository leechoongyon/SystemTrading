'''
Created on 2016. 7. 23.

@author: lee
'''

import scipy.optimize as spo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def f(X):
    Y = (X - 1.5) ** 2 + 0.5
    print "X = {}, Y = {}".format(X, Y)
    return Y

def test_run():
    Xguess = 2.0
    min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp':True})
    print "Minima found at:"
    print "X = {}, Y = {}".format(min_result.x, min_result.fun)
    
    # Plot function values, mark minima
    Xplot = np.linspace(0.5, 2.5, 21)
    Yplot = f(Xplot)
    plt.plot(Xplot, Yplot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.title("Minima of an objective function")
    plt.show()
    
if __name__ == '__main__':
    test_run()