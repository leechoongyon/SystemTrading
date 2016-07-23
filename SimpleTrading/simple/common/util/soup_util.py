# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 19.

@author: lee
'''
import urllib2

'''
    한 줄씩 읽어서 출력 
    참조  http://stackoverflow.com/questions/8020834/read-contents-of-script-with-beautifulsoup
'''

def interate(): 

    url_string = 'http://www.google.com/finance/historical?q={0}'
    
    sock = urllib2.urlopen(url_string)
    ch = sock.read()
    sock.close()

    print '\n'.join(str(i) + '  ' + repr(line)
                for i,line in enumerate(ch.splitlines(True)))