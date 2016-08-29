# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 19.

@author: lee
'''

# http://devanix.tistory.com/296 참고

import re


# str의 old를 new로 변경



def sub(old, new, str):
    result = re.sub(old, new, str) 
    return result

if __name__ == '__main__':
    str = "120\t,213▼▲%월"
    print "before str : %s" , str
    old = "[,▼▲%월\t]"
    new = ""
    print sub(old, new, str)