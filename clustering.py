>>> from pylab import *
>>> from scipy.cluster.vq import*
>>> list1 = [88,74,96,85]
>>> list2 = [92,99,95,94]
>>> list3 = [91,87,99,95]
>>> list4 = [78,99,97,81]
>>> list5 = [88,78,98,84]
>>> list6 = [100,95,100,92]
>>> data = vstack((list1,list2,list3,list4,list5,list6))
>>> centroids,_=kmeans(data,2)
>>> result,_= vq(data,centroids)
>>> print result









from scipy.cluster.vq import kmeans,vq
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import datetime
>>> start = datetime(2014,7,1)
>>> end = datetime(2014,9,30)
listDji = ['AXP','BA','CAT','CSCO','CVX','DD','DIS','GE',
           'GS','HD','IBM','INTC','JNJ','JPM','KO','MCD','MMM',
           'MRK','MSFT','NKE','PFE','PG','T','TRV','UNH','UTX',
           'V','VZ','WMT','XOM']
>>> quotes = [[0 for col in range(90)]for row in range(30)]
>>> listTemp = [[0 for col in range(90)]for row in range(30)]
>>> for i in range(30):
...   quotes[i] = quotes_historical_yahoo(listDji[i], start, end)
days = len(quotes[0])
>>> for i in range(30):
...   for j in range(days-1):
...     if(quotes[i][j][2]and quotes[i][j+1][2] and (quotes[i][j+1][2]>=quotes[i][j][2])):
...        listTemp[i][j] = 1.0
...     else:
...        listTemp[i][j] = -1.0
... 
>>> data = vstack(listTemp)

>>> data = np.vstack(listTemp)
>>> centroids,_ = kmeans(data,4)
>>> result,_= vq(data,centroids)
