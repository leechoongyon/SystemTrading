'''
Created on 2016. 7. 9.

@author: lee
'''

import numpy as np

if __name__ == '__main__':
    a = np.random.rand(5,4)
    print "Array:\n",a
    
    a[:,3] = [1,2,3,4,5]
    print "\nModified : \n", a