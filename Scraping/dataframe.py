import pandas as pd

df = pd.DataFrame(columns=['date','time','open','high','low','close','volume','range'])
df.loc[len(df)] = [1,2,3,4,5,6,7,8]
df.loc[len(df)] = [1,2,3,4,5,6,7,8]
dfList = [df]
print(dfList)
print('here')
df = pd.DataFrame(columns=['date','time','open','high','low','close','volume','range'])
dfList.append(df)
print(dfList)
