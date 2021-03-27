# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:34:34 2021

@author: rvesalapu
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
     
    
@app.route('/')
def home():
    return render_template("index.html")

def Pred(to_predict_list): 
    to_predict = np.array(to_predict_list).reshape(1, 2) 
    loaded_model = pickle.load(open("credit-card-fraud-detection.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(float, to_predict_list))
        result = Pred(to_predict_list)
    if int(result)== 1:
        prediction ='It is a fradulent transaction'
    else :
        prediction ='It is not a fraudulant transaction' 
            
    return render_template("result.html", prediction = prediction) 
    
      
                  
if __name__ == "__main__":
    app.run(debug=True)   
