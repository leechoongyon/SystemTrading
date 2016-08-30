# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 18.

@author: lee
'''

import re
import unicodedata


'''
    ex) print multi_replace("94,100.00", {",":"", ".":""})
        9410000
'''

def multiReplace(str, rep):
    rep = dict((re.escape(k), v) for k, v in rep.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    str = pattern.sub(lambda m: rep[re.escape(m.group(0))], str)
    return str

def replace(str, old, new):
    
    temp_str = []
    if (type(str) == list):
        for s in str:
            s = s.replace(old, new)
            temp_str.append(s)
        return temp_str
    
    return str.replace(old, new)
    

def convertUnicodeToString(data):
    results = []
    if type(data) is list:
        for obj in data:
            if type(obj) is unicode:
                results.append(unicodedata.normalize("NFKD", obj).encode('ascii', 'ignore'))
            else:
                results.append(obj)
        return results
        
    return unicodedata.normalize("NFKD", data).encode('ascii', 'ignore')

def searchIndex(regex, str):
    m = re.search(regex, str)
    if m:
        return m.start()
    else:
        print "No regex in that string"


def isNumber(str):
    try:
        tmp = float(str)
        return True
    except ValueError:
        return False

def convertStringToNum(str):
    return float(str)

if __name__ == '__main__':

    # 
    str = "Hello"
    print searchIndex("\d", str)

#     print convertUnicodeToString(u"Klüft skräms inför på fédéral électoral große")
    
    '''
    str = [] 
    str.append("2016-01-01")
    str.append("2016-01-02")
    
    print replace(str, "-", "")
    '''
    
#     print multiReplace("94,100.00", {",":"", ".":""})