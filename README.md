# project-4-final

# Table of Contents

## A. Project 4 UFO Sightings
Use machine learning to predict.

1. static
    1. css
       1. styles
2. templates
    1. index.html
    2. results.html
3. model.py
4. model.pkl
5. app.py
6. ufo_sightings.ipynb
7. ufo_db.csv
8. Procfile
9. requirements.txt
10. License
11. ReadMe
12. UFOSightingsPPT_pt2.pdf

-----------
## Introduction

  There are many reported sightings of UFO, but is there a way to predict their appearances? This project tries to predict the shape of the UFO by location.

-----------
## Process

  - Used the UFO data pulled from project 3
  - Cleaned the data by removing null values and dropping some columns
  - Reduced the shapes to 2 types:light and dim
  - Light category: light, fireball, flash, flare
  - Dim category: circle, triangle, unknown, other, sphere, disk, oval, formation, changing, cigar, rectangle, cylinder, diamond, chevron, teardrop, egg, cone, cross, delta , changed, round, crescent, hexagon 
  - Encoded the categories so Light = 1 and Dim = 0
  - Used Standard Scaler
  - Tried Logistic Regression, Random Forest, and tensorflow
  - Logistic Regression had slightly better testing accuracy, but data has weak coorelation between category and location
  - Used flask to create the app
  - Deployed to heroku

-----------
## Problems during the project

  - Submissions are dependent on how the user enters the data-this created a wide variety of data types that needed to be cleaned
  - The varied entries limited the number of categories that could be used
  - Initially running the machine learning crashed the notebook due to RAMs being used(too many columns)
  - There is a very weak correlation between location and shape prediction
  - Prediction is currently overfitting


-----------
## Considerations

  - More time would like to try other categories to see if there's any correlation.
  - Would need to clean the data more and make it uniform.

-----------

## Resources:
1. UFO Sightings Website: http://www.nuforc.org/webreports.html
2. https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
