#Supporting material
# https://towardsdatascience.com/a-beginners-guide-to-sentiment-analysis-in-python-95e354ea84f6
from email.mime import image
from tokenize import String
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
from skimage import io
from datacleanse import *


import nltk
from nltk.corpus import stopwords
# For Wordcloud make sure that below is satisfied
# Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Ensure all these are installed in your machine - Visual C++ Build tools core features >> MSVC toolset C++ 2019 v142 (x86,x64), Visual C++ 2019 Redistributable Update, Windows 10 SDK (10.0.17763.0) for Desktop C++
from wordcloud import WordCloud

def analysis():
    dataCleanse()
    # Reading the review file
    df = pd.read_csv('reviewsData.csv')
    df.head()

    # Create stopword list:
    nltk.download('stopwords')
    wordstoignore = set(stopwords.words('english'))
    wordstoignore.update(["br", "href"])

    #Generating cloud of words
    textt = " ".join(review for review in df.review)
    cloudofwords = WordCloud(stopwords=wordstoignore).generate(textt)
    plt.imshow(cloudofwords, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('static/wordcloudoverall.png')
    #plt.show()

    #Generating Sentiment Analysis based on App ratings
    df = df[df['rating'] != 3]
    print(df['rating'])
    df['sentiment'] = df['rating'].apply(lambda rating :+1 if int(rating) > 3 else -1)

    # split df - positive and negative sentiment:
    positive = df[df['sentiment'] == 1]
    negative = df[df['sentiment'] == -1]

    wordstoignore.update(["bws", "app"]) 
    ## bws and app removed because they are common words that do not attribute to the sentiment
    pos = " ".join(review for review in positive.title)
    wordcloud2 = WordCloud(stopwords=wordstoignore).generate(pos)
    plt.imshow(wordcloud2, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('static/wordcloudpositive.png')
    #plt.show()

    neg = " ".join(review for review in negative.title)
    wordcloud3 = WordCloud(stopwords=wordstoignore).generate(neg)
    plt.imshow(wordcloud3, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('static/wordcloudnegative.png')
    #plt.show()

    # Plotting a graph of the reviews
    #histogram = px.histogram(x=df['rating'])
    #histogram.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
    #                  marker_line_width=1.5)
    #histogram.update_layout(title_text='Product Score')   

    #wordclouds = make_subplots(rows=3, cols=1)
    #wordclouds.add_trace(go.Image(z=io.imread('wordcloudoverall.png'),dx=2048,dy=2048),1,1)
    #wordclouds.add_trace(go.Image(z=io.imread('wordcloudnegative.png'),dx=2048,dy=2048),2,1)
    #wordclouds.add_trace(go.Image(z=io.imread('wordcloudpositive.png'),dx=2048,dy=2048),3,1)
    #wordclouds.update_layout(
    #    autosize=True,
    #    width=2500,
    #    height=2500,)
    #histogram.show()
    #wordclouds.show()

    print("<<<<<<<<<<<<<<<<<<<Boom, That's all for now folks!!!>>>>>>>>>>>>>>>>>>>")

if __name__ == '__main__':
    analysis()