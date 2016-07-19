import urllib,time,datetime

class Quote(object):
  
    DATE_FMT = '%Y-%m-%d'
    TIME_FMT = '%H:%M:%S'
  
    def __init__(self):
        self.symbol = ''
        self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))

    def append(self,dt,open_,high,low,close,volume):
        self.date.append(dt.date())
        self.time.append(dt.time())
        self.open_.append(float(open_))
        self.high.append(float(high))
        self.low.append(float(low))
        self.close.append(float(close))
        self.volume.append(int(volume))
      
    def to_csv(self):
        return ''.join(["{0},{1},{2},{3:.2f},{4:.2f},{5:.2f},{6:.2f},{7}\n".format(self.symbol,
        self.date[bar].strftime('%Y-%m-%d'),self.time[bar].strftime('%H:%M:%S'),
              self.open_[bar],self.high[bar],self.low[bar],self.close[bar],self.volume[bar]) 
              for bar in xrange(len(self.close))])
    
    def write_csv(self,filename):
        with open(filename,'w') as f:
            f.write(self.to_csv())
        
    def read_csv(self,filename):
        self.symbol = ''
        self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))
        for line in open(filename,'r'):
            symbol,ds,ts,open_,high,low,close,volume = line.rstrip().split(',')
            self.symbol = symbol
            dt = datetime.datetime.strptime(ds+' '+ts,self.DATE_FMT+' '+self.TIME_FMT)
            self.append(dt,open_,high,low,close,volume)
        return True

    def __repr__(self):
        return self.to_csv()

   
class GoogleQuote(Quote):
# Daily quotes from Google. Date format='yyyy-mm-dd'
    def __init__(self,symbol,start_date,end_date=datetime.date.today().isoformat()):
        super(GoogleQuote,self).__init__()
        self.symbol = symbol.upper()
        start = datetime.date(int(start_date[0:4]),int(start_date[5:7]),int(start_date[8:10]))
        end = datetime.date(int(end_date[0:4]),int(end_date[5:7]),int(end_date[8:10]))
        url_string = "http://www.google.com/finance/historical?q={0}".format(self.symbol)
        url_string += "&startdate={0}&enddate={1}&output=csv".format(
                          start.strftime('%b %d, %Y'),end.strftime('%b %d, %Y'))
        
        csv = urllib.urlopen(url_string).readlines()
        print csv
        csv.reverse()
        for bar in xrange(0,len(csv)-1):
            ds,open_,high,low,close,volume = csv[bar].rstrip().split(',')
            open_,high,low,close = [float(x) for x in [open_,high,low,close]]
            dt = datetime.datetime.strptime(ds,'%d-%b-%y')
            self.append(dt,open_,high,low,close,volume)
 
if __name__ == '__main__':
    q = GoogleQuote('kakao corp','2011-01-01')              # download year to date Apple data
    print q                                           # print it out
# q = GoogleQuote('orcl','2011-11-01','2011-11-30') # download Oracle data for February 2011
# q.write_csv('orcl.csv')                           # save it to disk
# q = Quote()                                       # create a generic quote object
# q.read_csv('orcl.csv')                            # populate it with our previously saved data
# print q                                           # print it out
  