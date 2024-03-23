import json
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

json_files = {
    "agriculture": "CSVfiles/Agriculture_dat.json",
    "aviation": "CSVfiles/file2.json",   
}

commercial_data = {
    "commercial": {
        "2013": {
            "emission": 3391,
            "offset": 1441
        },
        "2014": {
            "emission": 4222,
            "offset": 5543
        },
        "2015": {
            "emission": 8190,
            "offset": 7266
        },
        "2016": {
            "emission": 3962,
            "offset": 2838
        },
        "2017": {
            "emission": 1033,
            "offset": 4094
        },
        "2018": {
            "emission": 4344,
            "offset": 3752
        },
        "2019": {
            "emission": 1888,
            "offset": 690
        },
        "2020": {
            "emission": 8042,
            "offset": 4059
        },
        "2021": {
            "emission": 8339,
            "offset": 9745
        },
        "2022": {
            "emission": 6675,
            "offset": 9057
        },
        "2023": {
            "emission": 5804,
            "offset": 2176
        }
    }
}

@app.route('/')
def get_agriculture_json():
    # Check if file exists in the json_files dictionary
    print(json_files.keys())

    if 'agriculture' in json_files.keys():
        print("I'm here")
        # return "This is a response"
        # Corresponding JSON file path
        json_file_path = json_files['agriculture']

        # If file exists
        if os.path.exists(json_file_path):
            # Load the JSON data from file
            with open(json_file_path, 'r') as file:
                json_data = json.load(file)
            
            return jsonify(json_data)
        else:
            return jsonify({'error': 'File not found'}), 404
    else:
        return jsonify({'error': 'Invalid endpoint'}), 400
    
@app.route('/commercial', methods=['GET'])
def getCommercialData():
    return jsonify(commercial_data)

if __name__ == "__main__":
    app.run(debug=True)
