'''
Created on 2016. 7. 18.

@author: lee
'''

def replace(str, old, new):
    
    temp_str = []
    if (type(str) == list):
        for s in str:
            s = s.replace(old, new)
            temp_str.append(s)
        return temp_str
    
    return str.replace(old, new)
    


if __name__ == '__main__':

    
    str = [] 
    str.append("2016-01-01")
    str.append("2016-01-02")
    
    print replace(str, "-", "")