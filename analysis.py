#Supporting material
# https://towardsdatascience.com/a-beginners-guide-to-sentiment-analysis-in-python-95e354ea84f6
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
import plotly.offline as py
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px

import nltk
from nltk.corpus import stopwords
# For Wordcloud make sure that below is satisfied
# Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Ensure all these are installed in your machine - Visual C++ Build tools core features >> MSVC toolset C++ 2019 v142 (x86,x64), Visual C++ 2019 Redistributable Update, Windows 10 SDK (10.0.17763.0) for Desktop C++
from wordcloud import WordCloud

# Reading the review file
df = pd.read_csv('reviewsData.csv')
df.head()

# Plotting a graph of the reviews
fig = px.histogram(df, x="rating")
fig.update_traces(marker_color="turquoise",marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5)
fig.update_layout(title_text='Product Score')
fig.show()

# Create stopword list:
nltk.download('stopwords')
stopwords = set(stopwords.words('english'))
stopwords.update(["br", "href"])

#Generating cloud of words
textt = " ".join(review for review in df.review)
cloudofwords = WordCloud(stopwords=stopwords).generate(textt)
plt.imshow(cloudofwords, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloudoveral.png')
#plt.show()

#Generating Sentiment Analysis based on App ratings
df = df[df['rating'] != 3]
df['sentiment'] = df['rating'].apply(lambda rating : +1 if rating > 3 else -1)

# split df - positive and negative sentiment:
positive = df[df['sentiment'] == 1]
negative = df[df['sentiment'] == -1]

stopwords.update(["bws", "app"]) 
## bws and app removed because they are common words that do not attribute to the sentiment
pos = " ".join(review for review in positive.title)
wordcloud2 = WordCloud(stopwords=stopwords).generate(pos)
plt.imshow(wordcloud2, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloudpostive.png')
#plt.show()

neg = " ".join(review for review in negative.title)
wordcloud3 = WordCloud(stopwords=stopwords).generate(neg)
plt.imshow(wordcloud3, interpolation='bilinear')
plt.axis("off")
plt.savefig('wordcloudnegative.png')
#plt.show()

print("<<<<<<<<<<<<<<<<<<<Boom, That's all for now folks!!!>>>>>>>>>>>>>>>>>>>")