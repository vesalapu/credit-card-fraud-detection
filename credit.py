# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:04:52 2021

@author: rvesalapu
"""

from flask import Flask,request,render_template
#from flask_mail import Mail,Message
import pickle
import sklearn
import pandas as pd
import random
import numpy as np

app =Flask(__name__)

@app.route('/',methods = ['GET'])
def getContent():
    return render_template('index.html')

@app.route('/',methods = ['POST'])
def predict():
    
    print('Got data from client:',dict(request.get_json(force=True)))
    
    data= dict(request.get_json(force=True))
    
    with open('credit-card-fraud-detection.pkl','rb') as file:
        pickle_model = pickle.load(file)
    
    xTest = pd.read_csv('creditcard.csv') 
    
    try:
        time_data = float(data['time'].strip())
        amount_data = float(data['amount'].strip())
    except ValueError as e:
        return 'Invalid Data'
    
    pca_credit = xTest[(xTest['Time'] == float(data['time'])) & (xTest['amount'] ==float(data['amount']))]
    
    if(len(pca_credit) == 0):
        return 'Invalid Data'
    
    required = np.array(pca_credit)
    
    testData = required[0][:-1].reshape(1,-1)
    
    pickle_model.decision_function(testData)
    
    output = pickle_model.predict(testData)
    
    if(required[0][-1] == 1.0 and output == [-1]):
        return 'it seems to be a fraudulent transaction.'
    elif (required[0][-1] == 0.0 and output == [1]):
        return 'it is a normal transaction.'
    else:
        return 'it seems to be a fraudulent transaction.'
    
    
if __name__ == "__main__":
    app.run(debug=True)    
