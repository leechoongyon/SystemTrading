# -*- coding: utf-8 -*-
'''
Created on 2016. 7. 16.

@author: lee
'''

import datetime
import time

from dateutil import parser


def getToday():
    return datetime.datetime.today()

'''
    1. %Y%m%d -> 20160101
    2. %Y-%m-%d -> 2016-01-01
'''  


def getTodayWithFormatting(format):
    return getToday().strftime(format)

'''
    time.time(), -700
'''

def getDayFromSpecificDay(day, num, format):
     return datetime.date.fromtimestamp(day + num * 60 * 60 * 24).strftime(format)

def convertDatetimeToTime(datetime):
    return time.mktime(datetime.timetuple())


# 2012-02-02(str) -> 2012-02-02(datetime)
def convertStringToDatetime(str, format):
    return datetime.datetime.strptime(str, format)

# Jan 15, 2014(str) -> 2014-01-15(datetime)
# ex) convert_string_to_datetime2("Aug 28, 2000", "%Y-%m-%d")
# 2000-8-28
def convertStringToDatetime2(str, format):
    dt = parser.parse(str)
    return dt.strftime(format)

def convertStringToTime(str, format):
    date_time = convertStringToDatetime(str, format)
    time = convertDatetimeToTime(date_time)
    return time

'''
    오늘로부터 이전, 지난 날짜를 구함.
'''



if __name__ == '__main__':
    
    '''
    temp_day = "20160620"
    date_time = datetime.datetime.strptime(temp_day, "%Y%m%d")
    time = convert_datetime_to_time(date_time)
    print get_day_from_specific_day(time, 1)
    '''
    
    print getTodayWithFormatting("%Y%m%d")
    print getDayFromSpecificDay(time.time(), -700, "%Y%m%d")
    '''
    yesterday = datetime.date.fromtimestamp(time.time() - 1*60*60*24)
    today = datetime.date.fromtimestamp(time.time())
    start = datetime.datetime(yesterday.year, yesterday.month, yesterday.day)
    end = datetime.datetime(today.year, today.month, today.day)
    
    print start
    print end
    '''