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
    return "This is the prediction route"

df = pd.read_csv('../CSVfiles/ForPrediction/agriculture_pred.csv')

# columnsList = list(df.columns[1:])
# columnsList = [int(year.split()[0]) for year in columnsList]

# print(columnsList, "\n===========================================\n", list(df[df.columns[1]]))
# print("\n===========================================\n", df.iloc[1])

print(df)
X = sm.add_constant(df["year"])  # Add constant term
model = sm.OLS(df["emission"], X).fit()

# Predict carbon emission for 2024
predicted_emission_2024 = model.predict([1, 2024])
print(f"Predicted carbon emission for 2024: ", predicted_emission_2024)