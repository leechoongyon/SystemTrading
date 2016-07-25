# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 23.

@author: lee
'''

import scipy.optimize as spo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def error(line, data): 
    err = np.sum((data[:,1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err
