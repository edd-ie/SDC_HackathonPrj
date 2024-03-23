import json
from flask import Flask, jsonify, request, Blueprint
import os
import app
import pandas as pd
# from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm

app = Blueprint('predictions', __name__)

@app.route('/prediction')
def index():
    data = {'agriculture' : get_prediction("agriculture"),
            'aviation' : get_prediction("aviation"),
            'commercial' : get_prediction("commercial"),    
            'energy' : get_prediction("energy"),
            'forestry' : get_prediction("forestry"),
            'industrial' : get_prediction("industrial"),
            'marine' : get_prediction("marine"),
            'residential' : get_prediction("residential"),
            'transport' : get_prediction("transport"),
            'waste' : get_prediction("waste"),}
    return json.dumps(data)

def get_prediction(fileName):
    df = pd.read_csv(f"CSVfiles/ForPrediction/{fileName}_pred.csv")

    #print(df)
    X = sm.add_constant(df["year"])  # Add constant term
    model = sm.OLS(df["emission"], X).fit()

    predicted_emission_2024 = model.predict([1, 2024])
    returnVal = predicted_emission_2024
    return predicted_emission_2024
    #print(f"Predicted carbon emission for 2024: ", predicted_emission_2024)