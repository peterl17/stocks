import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

apiKey = 'OGDIFJ29G7HTQQUT'
_domain = 'https://www.alphavantage.co/query?function='
functions = ['TIME_SERIES_INTRADAY','TIME_SERIES_DAILY','TIME_SERIES_DAILY_ADJUSTED','SECTOR','GLOBAL_QUOTE']
intervals = ['1min', '5min', '15min', '30min', '60min']
outputSizes = ['compact', 'full']
outputSize = outputSizes[1]
interval = intervals[1]
function = functions[0]
SYMBOL = 'SPY'
response = requests.get('{}{}&symbol={}&interval={}&outputsize={}&apikey={}'.format(_domain,function,SYMBOL,interval,outputSize,apiKey))
data = response.json()
data = data['Time Series ({})'.format(interval)]

#dataframe
df = pd.DataFrame(columns=['date','time','open','high','low','close','volume','range'])
dataframes = []
flagLastDate = True
for dt,values in data.items():
    # dt = 2019-03-06 14:21:00
    # p = {'1. open': '277.3400', '2. high': '277.4100', '3. low': '277.3200', '4. close': '277.3700', '5. volume': '710380'}

    datetime = datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
    date = datetime.date()
    if(flagLastDate == False):
        if(date != lastDate):
            dataframes.append(df)
            print('here')
            df = pd.DataFrame(columns=['date','time','open','high','low','close','volume','range'])
    flagLastDate = False
    lastDate = date
    time = datetime.time()
    row = [date, time,float(values['1. open']), float(values['2. high']),
          float(values['3. low']),float(values['4. close']), int(values['5. volume']), float(values['2. high'])-float(values['3. low'])]
    df.loc[len(df)] = row

for eachDF in dataframes:
    print(eachDF)
    eachDF.plot.line(x='time', y='high')
plt.show(block=True)

#df.to_csv('/Users/peterluo/Downloads/SPY_Data_{}.csv'.format(date.date()))

