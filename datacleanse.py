# The app reviews for BWS on Tapp can be found here
# https://itunes.apple.com/au/rss/customerreviews/id=1463355630/json
# https://rstudio-pubs-static.s3.amazonaws.com/144219_cdfba94f3f4d42a1b582c0b69a60cf78.html

import json
from os import write
import requests

#Programatically fetch reviews from itunes
#Everydayrewards
#appID = 1489403660
#Woolies
#appID = 975089690
#BWS
#appID = 1463355630
#Dans
appID = 708912408
appReviewUrl = "https://itunes.apple.com/au/rss/customerreviews/page={0}/id={1}/sortBy=mostRecent/json"
print("Beginning to fetch reviews from iTunes")
writeAppReviews = open("reviewsData.csv","a", encoding="utf8")
writeAppReviews.write("timestamp"+","+"rating"+","+"title"+","+"review"+"\n")
for pagenum in range(1,11):
    appReviewUrl = appReviewUrl.format(pagenum, appID)
    r = requests.get(url=appReviewUrl)
    data = r.json()
    #readAppReviews = open("iOSAppReviews.json", "r", encoding="utf8")
    #jsonObject = json.loads(readAppReviews.read())
    reviews = data["feed"]["entry"]
    print("Page: "+str(pagenum)+" ; Reviews: "+str(len(reviews)))
    if len(reviews) > 0:
        for review in reviews:
            reviewTitle = review["title"]["label"]
            reviewDescription = review["content"]["label"]
            writeAppReviews.write(review["updated"]["label"]+
            ","+review["im:rating"]["label"]+
            ","+reviewTitle.replace("\n","").replace(",","")+
            ","+reviewDescription.replace("\n","").replace(",","")+
            "\n")      
print("<<<<<<<<<<<<<<<<<<<<<<<<Task Completed>>>>>>>>>>>>>>>>>>>>>>>>>")