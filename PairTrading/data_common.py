import pandas
import pandas.io.data
import datetime
import urllib2
import csv

import pandas as pd
import pandas.io.data as web

def get_quote_today(symbol):
    url="http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=d1t1ohgl1vl1"

    new_quote= pd.read_csv(url%symbol, 
                          names=[u'Date',u'time',u'Open', u'High', u'Low', 
                                 u'Close', u'Volume', u'Adj Close'])

    # generate timestamp: 
    stamp = pd.to_datetime(new_quote.Date+" "+new_quote.time)
    new_quote.index= stamp
    return new_quote.iloc[:, 2:]


if __name__ == "__main__":
    symbol = "TSLA"

    history = web.DataReader(symbol, "yahoo", start="2014/1/1")
    print history.tail()
    new_quote = get_quote_today(symbol)
    if new_quote.index > history.index[-1]:
        if new_quote.index[-1].date() == history.index[-1].date():
            # if both quotes are for the first date, update history's last record. 
            history.iloc[-1]= new_quote.iloc[-1]
        else:
            history=history.append(new_quote)
    history.tail()
