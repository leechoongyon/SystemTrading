# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 16.

@author: lee
'''

import datetime
import time

def get_today():
    return datetime.datetime.today()

'''
    1. %Y%m%d -> 20160101
    2. %Y-%m-%d -> 2016-01-01
'''  
def get_today_with_formatting(format):
    return get_today().strftime(format)

def convert_datetime_to_time(datetime):
    return time.mktime(datetime.timetuple())

def convert_string_to_datetime(str, format):
    return datetime.datetime.strptime(str, format)

def convert_string_to_time(str, format):
    date_time = convert_string_to_datetime(str, format)
    time = convert_datetime_to_time(date_time)
    return time

'''
    오늘로부터 이전, 지난 날짜를 구함.
'''
def get_day_from_specific_day(day, num, format):
     return datetime.date.fromtimestamp(day + num * 60 * 60 * 24)


if __name__ == '__main__':
    temp_day = "20160620"
    date_time = datetime.datetime.strptime(temp_day, "%Y%m%d")
    time = convert_datetime_to_time(date_time)
    print get_day_from_specific_day(time, 1)
