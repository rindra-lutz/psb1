
import numpy as np
import streamlit as streamlit
import matplotlib.pyplot as plt
import pandas as pd

# Datas
data = pd.read_csv(r"D:\Hadoop\Data.csv")

# Configuration
streamlit.set_page_config(layout='wide')
streamlit.title('Utilisation of Youtube')

# Variables
def count_rows(rows):
    return len(rows)

selected_number = 5
select_years = []
By_years = data.groupby('year')['year'].count().sort_values(ascending=False).index
select_years.append(streamlit.selectbox('Select a year :', By_years))

lastYear = select_years[0] - 1
# we put it in a ARRAY to use 'isin'
lastYearTab = [lastYear]
nbview = data[data['year'].isin(select_years)]
nbviewLastYear = data[data['year'].isin(lastYearTab)]
By_month = nbview.groupby(['year','month']).apply(count_rows)
url = nbview.groupby('titleUrl')['year'].count().sort_values(ascending = False).index[0]

streamlit.info(f'In the year {select_years[0]}, this is what happened !')

vide1, vide2, vide3 = streamlit.columns(3);
with vide1:
    streamlit.metric(label="I have seen", value=f'{nbview.shape[0]} videos', delta= f'{nbview.shape[0] - nbviewLastYear.shape[0]} compared to {lastYearTab[0]}')
with vide2:
    streamlit.subheader('And this is my most watched')
    streamlit.video(f'{url}', format="video/mp4", start_time=0)



numberOfViewPerHour, numberOfViewPerDay, numberOfViewPerMounth = streamlit.columns(3)
with numberOfViewPerHour:
    streamlit.caption('Number of view per hour')
    hist_values1 = np.histogram(nbview['hour'],bins=24, range=(1,24))[0]
    streamlit.bar_chart(hist_values1)
with numberOfViewPerDay:
    streamlit.caption('Number of view per day')
    hist_values2 = np.histogram(nbview['day'],bins=31, range=(1,31))[0]
    streamlit.line_chart(hist_values2)
with numberOfViewPerMounth:
    streamlit.caption('Number of view per month')
    labels = ['January', 'February','March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig1, ax1 = plt.subplots()
    ax1.pie(By_month, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90)
    ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
    streamlit.pyplot(fig1)


vide1, mostWordsInTitles, vide3, mostWordsInTitles, vide5 = streamlit.columns(5)

#
# 
# 
### THE FOLLOWING CODE DIDN'T WORK DUE TO A "TO RECENT VERSION OF MY PYTHON"
### I JUST TRIED TO DO A WORDCLOUD OF THE TITLES OF THE VIDEOS I HAVE SEEN
# 
# 
#!pip install nltk
#import nltk
#nltk.download('punkt')

#from collections import Counter
#from nltk.corpus import stopwords
#import string

#!pip install wordcloud
#from wordcloud import WordCloud
#from wordcloud import STOPWORDS
#import matplotlib.pyplot as plt

#data["title"]=data["title"].astype(str)

#destination = []
#for i in range(len(data)):
#    destination.append(data.loc[i,"title"])

#all_tokens1 = []
#for line in destination:
#    for mot in line.split():
#        all_tokens1.append(mot)
        
#total_term_frequency = Counter(all_tokens1)

#tfdict = {}
#for w, f in total_term_frequency.most_common():
    
#    relative_tf = f / sum(list(total_term_frequency.values())) # nobre relative
#    tfdict[w]  = relative_tf


#   wordcloud = WordCloud(
#                            stopwords=STOPWORDS,
#                            background_color='black',
#                            mode = 'RGB',
#                            max_words=1000,
#                            width=1000,
#                            height=1000
#                            ).generate_from_frequencies(tfdict)
#    plt.imshow(wordcloud, interpolation='bilinear')
#    plt.axis('off')
#st.set_option('deprecation.showPyplotGlobalUse', False)
#st.pyplot()

