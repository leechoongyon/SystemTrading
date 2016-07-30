'''
Created on 2016. 7. 24.

@author: lee
'''

import scipy.optimize as spo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def error(line, data):
    err = np.sum((data[:,1] - (line[0] * data[:,0] + line[1])) ** 2)
    
    
def test_run():
    l_orig = np.float32([4,2])
    print "Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1])
    Xorig = np.linspace(0, 10, 21)
    Yorig = l_orig[0] * Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original line")
    
    noise_sigma = 3.0
    noise = np.random.normal(0, noise)