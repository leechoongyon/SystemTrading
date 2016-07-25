'''
Created on 2016. 7. 18.

@author: lee
'''
import re


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
    


if __name__ == '__main__':

    '''
    str = [] 
    str.append("2016-01-01")
    str.append("2016-01-02")
    
    print replace(str, "-", "")
    '''
    
    print multiReplace("94,100.00", {",":"", ".":""})