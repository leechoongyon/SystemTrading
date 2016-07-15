'''
Created on 2016. 7. 9.

@author: lee
'''

import numpy as np

if __name__ == '__main__':
    a = np.array([(20,25,10,23,26,32,10,5,0), (0,2,50,20,0,1,28,5,0)])
    print a
    
    mean = a.mean()
    print mean
    
    a[a<mean] = mean
    print a