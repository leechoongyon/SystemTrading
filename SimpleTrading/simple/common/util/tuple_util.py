'''
Created on 2016. 6. 30.

@author: lee
'''

def replaceAtIndex1(tup, ix, val):
    lst = list(tup)
    lst[ix] = val
    return tuple(lst)

def replaceAtIndex2(tup, ix, val):
    return tup[:ix] + (val,) + tup[ix+1:]

def convertDatetimeToStr(tup, ix):
    lst = list(tup)
    lst[ix] = lst[ix].strftime("%Y%m%d")
    return tuple(lst)

def addElement(tup, ix, val):
    tempList = list(tup)
    tempList.insert(ix, val)
    return tuple(tempList)

if __name__ == '__main__':
    rows = []
    row = ('a', 'b', 'c', 'd')
    rows.append(row)
    print rows
    for row in rows:
        row = addElement(row, 0, '0')
    print row
    