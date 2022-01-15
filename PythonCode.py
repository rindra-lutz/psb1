
### PREPARATION CODE ON GOOGLE COLAB


#imports
import json
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import dates
import datetime

from google.colab import drive
drive.mount('/content/drive')

### Datas
dt = pd.read_json("/content/drive/My Drive/watch-history.json")
dt.to_csv('watch-history.csv',index = None)

df = pd.read_csv('watch-history.csv')

### Configuration
df = df[df['title'] != 'Vous avez regardé une vidéo qui a été supprimée']
df = df[df['titleUrl'] != 'NaN']
df = df[df['titleUrl'] != 'nan']

column_with_nan = df.columns[df.isnull().any()]
df.shape
for column in column_with_nan:
    print(column, df[column].isnull().sum())

for column in column_with_nan:
    if df[column].isnull().sum()*100.0/df.shape[0] > 80:
            df.drop(column,1, inplace=True)

df.shape

df.describe()

df.info()

df['Time']=df['time'].map(pd.to_datetime)

def get_weekday(dt):
    return dt.weekday()
def get_dom(dt):
    return dt.day
def get_hour(dt):
    return dt.hour
def get_minute(dt):
    return dt.minute
def get_second(dt):
    return dt.second
def get_year(dt):
    return dt.year
def get_month(dt):
    return dt.month

df['weekday']=df['Time'].map(get_weekday)
df['day']=df['Time'].map(get_dom)
df['hour']=df['Time'].map(get_hour)
df['minute']=df['Time'].map(get_minute)
df['seconde']=df['Time'].map(get_second)
df['year']=df['Time'].map(get_year)
df['month']=df['Time'].map(get_month)

df = df.drop(["time","products", "activityControls"],axis=1)
df

df["subtitles"] = df["subtitles"].astype(str)
df["Channel"]=df["subtitles"].apply(lambda x : x.split(",")[0])
df

df.loc[0,"Channel"].replace("[{'name':", "")
df["Channel"]=df["Channel"].apply(lambda x : x.replace("[{'name': ", ""))


df.loc[0,"Channel"].replace("'", "")
df["Channel"]=df["Channel"].apply(lambda x : x.replace("'", ""))
df

df.head(50)

### Graphs

histo=df["day"].plot.hist(bins=30,rwidth=0.8, range=(0.5,30.5), title = "Frequency by days of the months - Youtube - since 2019")
plt.xlabel('days of the month');

df_3 = df['title'].value_counts()

def count_rows(rows):
    return len(rows)

by_date = df.groupby(['year','month']).apply(count_rows)
by_date

by_date.plot.line(color='red', figsize=(30,10))
plt.title('Number of videos since April 2019')
plt.xlabel('Months and years')
plt.ylabel('Number of videos seen')
;

import seaborn as sns

group_hours= df.groupby(["hour"]).count()

group_hours.plot(figsize=(15,10))

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

plt.subplot(1,3,1)
plt.plot(df.groupby(['hour']).count()['header'],color='b')
plt.title('Utilisation by hour')

plt.subplot(1,3,2)
plt.plot(df.groupby(['month']).count()['header'],color='g')
plt.title('Utilisation by month')

plt.subplot(1,3,3)
plt.plot(df.groupby(['year']).count()['header'],color='r')
plt.title('Utilisation by year')
plt.show()  

df.groupby(["year","month"]).count()    

df_group = df.groupby(["year","month"]).count()
df_group[df_group.index.get_level_values('year').isin([2020])]

