from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model = pickle.load(open('credit-card-fraud-detection.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])

def predict():
    if request.method == 'POST':
        Amount = float(request.form['Amount'])
        Time   = float(request.form['Time'])
        
        prediction = model.predict([[Amount,Time]])
        
        if prediction == 1:
            return render_template('index.html',prediction_text = "It is a fraudulant transaction")
        else:
            return render_template('index.html',prediction_text = "It is not a fraudulant transaction")
                                   
        
    else:
        return render_template('index.html')
        
 
if __name__=="__main__":
    app.run(debug=True)