import json
from flask import Flask, jsonify, request
import os
from flask_cors import CORS
import predictons

app = Flask(__name__)
CORS(app)

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

@app.route('/')
def index():
    return "This is the base route"

@app.route('/<sector>')
def get_agriculture_json(sector):
    # Check if file exists in the json_files dictionary
    # return loadJsonFiles("agriculture")
    if(sector != "agriculture" and sector != "commercial" and sector != "energy" and sector != "aviation" and sector != "forestry" and sector != "industrial" and sector != "marine" and sector != "residential" and sector != "transporation" and sector != "waste"):
        return "Invalid route"
    return loadJsonFiles(sector)

if __name__ == "__main__":
    app.run(debug=True)
    
