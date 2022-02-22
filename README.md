# purpose
Purpose of this project is to do sentiment analysis of app based on app reviews and generate a wordloud showing positive, negative and overall sentiments. Project is already soing sentiment analysis for BWS app. To do sentiment analysis on your own project, follow instructions in README.

# appreviews
Install Python and python package installer PIP module in your machine
  **MAC :** 
  brew install python3
  Note: pip3 will get automatically installed (In commands, use pip3 instead of pip)

Clone the project and run the below commands in sequence.

Find out the app id of a desired app from itunes website using the below steps.
1. Go to https://www.apple.com/itunes/
2. Search for the desired app and and select the app from search results.
3. Once on the app details page, grab the digits in the url that come after "/id*********" here everything after id is the app id.
4. Now in the appid.json file in line# 2 change the app id to the app id from above step and save your changes.

Stopwords: While doing sentiment analysis we dont want name of app to be included in wordcloud. To do sp, please add desired stopwords at line no 52 in analysis.py 


# Installs all python packages required for the analytics
pip install -r requirements.txt

# Generates the app reviews from itunes for the given app id. Reviews are for the last 500 reviews.
python datacleanse.py

# Run the analytics and generate the visualizations
python analysis.py

# Output
Once the analysis has run successfully, you will see a new tab in browser with graph showing categorization on basis of no of ratings
Also, you will see wordcloud images in project directory. You can take a look and analyze sentiments of your customers and work on that area.

# Roadmap
1. Put in URL of app and stopwords(words not to be analyzed)
2. DO sentiment analysis of Android apps

# Common issues
You may get issues on Apple M1 as wordcloud library may not work. To fix those issues we have to activate conda environment which can be done by folllowing steps below:
  brew install miniforge
  conda activate 
  conda init zsh (Only If you get erros and are asked to choose an environment then run and restart shell)
  try running analyius again.
  
