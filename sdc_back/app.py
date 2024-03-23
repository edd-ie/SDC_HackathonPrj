import json
from flask import Flask, jsonify, request
import os
from flask_cors import CORS
<<<<<<< HEAD
=======
# import predictons
>>>>>>> 849cc246e6cfe132a141f2ecae27737001783de0

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

@app.route('/sector/<sectorName>')
def get_agriculture_json(sectorName):
    # Check if file exists in the json_files dictionary
    # return loadJsonFiles("agriculture")
    if(sectorName != "agriculture" and sectorName != "commercial" and sectorName != "energy" and sectorName != "aviation" and sectorName != "forestry" and sectorName != "industrial" and sectorName != "marine" and sectorName != "residential" and sectorName != "transporation" and sectorName != "waste"):
        return "Invalid route"
    return loadJsonFiles(sectorName)

if __name__ == "__main__":
    app.run(debug=True)
    
