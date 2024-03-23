import json
from flask import Flask, jsonify, request, Blueprint, render_template, session, abort
import os
from flask_cors import CORS
from predictons import app

mainApp = Flask(__name__)
mainApp.register_blueprint(app)

CORS(mainApp)

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


jsonFilePath = os.path.join(parent_directory, "CSVfiles/sector.json")

def loadJsonFiles(sector):
    # If file exists
    print(jsonFilePath)
    if os.path.exists(jsonFilePath):
        # Load the JSON data from file
        with open(jsonFilePath, 'r') as file:
            json_data = json.load(file)
            sectorJson = json_data[sector]
            # print(agriculture)
                
        return jsonify(sectorJson)
    else:
        return jsonify({'error': 'File not found'}), 404

@mainApp.route('/')
def index():
    return "This is the base route"

@mainApp.route('/sector/<sectorName>')
def get_agriculture_json(sectorName):
    # Check if file exists in the json_files dictionary
    # return loadJsonFiles("agriculture")
    if(sectorName != "agriculture" and sectorName != "commercial" and sectorName != "energy" and sectorName != "aviation" and sectorName != "forestry" and sectorName != "industrial" and sectorName != "marine" and sectorName != "residential" and sectorName != "transporation" and sectorName != "waste" and sectorName != "total"):
        return "Invalid route"
    return loadJsonFiles(sectorName)

@mainApp.route('/sector/<tax>')
def get_agriculture_json(sectorName):
    # Check if file exists in the json_files dictionary
    # return loadJsonFiles("agriculture")
    if(sectorName != "taxInfo"):
        return "Invalid route"
    return loadJsonFiles(sectorName)

@mainApp.route('/sector/<future>')
def get_agriculture_json(sectorName):
    # Check if file exists in the json_files dictionary
    # return loadJsonFiles("agriculture")
    if(sectorName != "offset_providers"):
        return "Invalid route"
    return loadJsonFiles(sectorName)

if __name__ == "__main__":
    mainApp.run(debug=True)
    
