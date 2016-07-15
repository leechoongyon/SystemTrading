# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 9.

@author: lee
'''

import numpy as np

if __name__ == '__main__':
    a = np.random.rand(5,4)
    print "Array:\n", a
    
    # row는 전체 범위, columns는 0~3범위에서 뒤에서 1만큼 자르겠다?
    print a[:,0:3:1]    