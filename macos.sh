#!/bin/sh

#removing previously generated artefacts from this project if any
rm -f reviewsData.csv wordcloudnegative.png wordcloudpositive.png wordcloudoverall.png

#Generating the reviews file
python3 datacleanse.py

#Performing analysis on ratings and sentiment analysis
python3 analysis.py