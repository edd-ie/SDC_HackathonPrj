import json
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

json_files = {
    "agriculture": "CSVfiles/Agriculture_dat.json",
    "aviation": "CSVfiles/file2.json",   
}

@app.route('/')
def get_agriculture_json():
    # Check if file exists in the json_files dictionary
    if 'agriculture' in json_files:
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

if __name__ == "__main__":
    app.run(debug=True)
