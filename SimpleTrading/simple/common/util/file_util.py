'''
Created on 2016. 7. 23.

@author: lee
'''
import os


def mkdir(dirPath):
    if not os.path.isdir(dirPath):
        os.mkdir(dirPath)

if __name__ == '__main__':
    print os.path.dirname('SimpleTrading')
    print os.path.basename('.')
#     print os.path.dirname('./')
    print os.path.expanduser('SimpleTrading')