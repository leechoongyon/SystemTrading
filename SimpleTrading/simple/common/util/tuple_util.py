'''
Created on 2016. 6. 30.

@author: lee
'''


def replace_at_index1(tup, ix, val):
    lst = list(tup)
    lst[ix] = val
    return tuple(lst)

def replace_at_index2(tup, ix, val):
    return tup[:ix] + (val,) + tup[ix+1:]

def convert_datetime_to_str(tup, ix):
    lst = list(tup)
    lst[ix] = lst[ix].strftime("%Y%m%d")
    return tuple(lst)