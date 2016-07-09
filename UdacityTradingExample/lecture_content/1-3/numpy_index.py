'''
Created on 2016. 7. 9.

@author: lee
'''

import numpy as np

if __name__ == '__main__':
    a = np.random.rand(5)
    
    print "Array : \n", a
    indices = np.array([1,1,2,3])
    
    print "\nSelected Array : \n", a[indices] 
