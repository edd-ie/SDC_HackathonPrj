import json
from flask import Flask, jsonify, request, Blueprint
import os
import app

app = Blueprint('predictions', __name__)

@app.route('/prediction')
def index():
    return "This is the prediction route"