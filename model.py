# Simple Linear Regression

'''
This model predicts the salary of the employ based on experience using simple linear regression model.
'''

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Importing the dataset
dataset = pd.read_csv('./ufo_db.csv',header = 0, sep = ',')
X = dataset.drop(["Category"], axis="columns").values
y = dataset["Category"].values

# Splitting the dataset into the Training set and Test set
scaler= StandardScaler()
X_scaled = scaler.fit_transform(X)
#print(X_scaled)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=1)
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
#print(X_train_scaled)


# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train_scaled, y_train)

# Predicting the Test set results
#y_pred = classifier.predict(X_test)

# Saving model to disk
pickle.dump(classifier, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load( open('model.pkl','rb'))
data =[[33.60028, -117.70854]]
data = scaler.transform(data)
prediction = classifier.predict(data)
print(prediction)