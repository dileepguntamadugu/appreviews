# appreviews
Install Python and python package installer PIP module in your machine

Clone the project and run the below commands in sequence

Find out the app id of a desired app from itunes website using the below steps.
1. Go to https://www.apple.com/itunes/
2. Search for the desired app and and select the app from search results.
3. Once on the app details page, grab the digits in the url that come after "/id*********" here everything after id is the app id.
4. Now in the appid.json file in line# 2 change the app id to the app id from above step and save your changes.


# Installs all python packages required for the analytics
pip install -r requirements.txt

# Generates the app reviews from itunes for the given app id. Reviews are for the last 500 reviews.
python datacleanse.py

# Run the analytics and generate the visualizations
python analysis.py
