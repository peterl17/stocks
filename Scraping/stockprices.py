from _datetime import datetime as dt
from _datetime import date, time, timedelta, datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
yesterdayDate = date.today() - timedelta(days= 1);
start = dt.combine(yesterdayDate, time.min)
end = dt.today()

#df = dataframe
df = web.DataReader('F', 'morningstar', start, end)

print(df.tail());