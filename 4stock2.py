#stock max
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import datetime
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

start = datetime(2014,1,1)
end = datetime(2014,12,31)
quotesMS = quotes_historical_yahoo_ochl('MSFT', start, end)
quotesIntl = quotes_historical_yahoo_ochl('INTC', start, end)
fields = ['date','open','close', 'high', 'low', 'volume']
#quotedfMS = pd.DataFrame(quotesMS, columns= fields)
list1 = []
for i in range(0, len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x, '%Y-%m-%d')
    list1.append(y)
list2 = []
for i in range(0, len(quotesIntl)):
    x = date.fromordinal(int(quotesIntl[i][0]))
    y = date.strftime(x, '%Y-%m-%d')
    list2.append(y)
quotedfMS = pd.DataFrame(quotesMS, index = list1, columns= fields)
quotedfMS = quotedfMS.drop(['date'], axis = 1)

quotedfIntl = pd.DataFrame(quotesIntl, index = list2, columns= fields)
quotedfIntl = quotedfIntl.drop(['date'], axis = 1)

listmonth1 = []
for i in range(0,len(quotedfMS)):
     temp  = time.strptime(quotedfMS.index[i],"%Y-%m-%d")
     listmonth1.append(temp.tm_mon)
listmonth2 = []
for i in range(0,len(quotedfIntl)):
     temp  = time.strptime(quotedfIntl.index[i],"%Y-%m-%d")
     listmonth2.append(temp.tm_mon)

tempMSdf = quotedfMS.copy()
tempMSdf['month'] = listmonth1
closemaxMS = tempMSdf.groupby('month').max().close
listMS = []
for i in range(1,13):
   listMS.append(closemaxMS[i])
listMSIndex = closemaxMS.index

print (str(len(listMS))+'listMS')
print (str(len(listMSIndex))+'listMSIndex')

tempIntldf = quotedfIntl.copy()
tempIntldf['month'] = listmonth2
closemaxIntl = tempIntldf.groupby('month').max().close
listIntl = []
for i in range(1,13):
   listIntl.append(closemaxIntl[i])
listIntlIndex = closemaxIntl.index

print (str(len(listIntl))+'listIntl')
print (str(len(listIntlIndex))+'listIntlIndex')

plt.subplot(211)
plt.plot(listMSIndex,listMS,color='r',marker='o')
plt.subplot(212)
plt.plot(listIntlIndex,listIntl,color='green',marker='o')

plt.show()
