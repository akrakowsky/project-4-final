# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
from sklearn import preprocessing

app = Flask(__name__)

# Load the model
model = pickle.load(open('./model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        #label_encoder =LabelEncoder()
        #model['Category']= label_encoder.fit_transform(model['Category'])
        #data = request.get_json(force=True)
        print(request.form['LATITUDE'])
        data1 = float(request.form['LATITUDE'])
        print(request.form['LONGITUDE'])
        data2 = float(request.form['LONGITUDE'])
        print("Data", model.predict([[data1, data2]]))
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([[data1, data2]])

        # Take the first value of prediction
        #output = list(label_encoder.inverse_transform(prediction))[0]
        output = prediction
        return render_template("results.html", output=output, exp=[data1, data2])
        
if __name__ == '__main__':
    app.run(debug=True)
