import json

# Provided data
emissions_data = {
    "Agriculture": [8811, 7318, 2210, 2820, 7064, 7111, 4003, 5703, 1763, 6367, 5957],
    "Aviation": [4038, 4168, 4039, 6396, 9416, 4115, 9182, 6797, 6791, 4155, 8098],
    "Commercial": [3391, 4222, 8190, 3962, 1033, 4344, 1888, 8042, 8339, 6675, 5804],
    "Energy": [4158, 8232, 7487, 6937, 8899, 6258, 3384, 7949, 6560, 5247, 5587],
    "Forestry": [4327, 5797, 4712, 9477, 7794, 2883, 8510, 1513, 9780, 8171, 8077],
    "Industrial": [6163, 2883, 5084, 9199, 6718, 3831, 6241, 6320, 7207, 1817, 4404],
    "Marine": [3621, 7164, 4654, 5675, 3656, 1229, 2089, 6505, 2272, 8000, 4607],
    "Residential": [2046, 7948, 9766, 8615, 7336, 1727, 4292, 1486, 1011, 1332, 2724],
    "Transportation": [1093, 8238, 4016, 2930, 1567, 8223, 2401, 9836, 5637, 3595, 6892],
    "Waste": [5439, 9141, 8371, 8718, 1608, 4884, 5959, 4998, 5897, 7818, 5380]
}

offset_data = {
    "Agriculture": [5398, 3261, 121, 6395, 6011, 6434, 5946, 9753, 5039, 6677, 7353],
    "Aviation": [2278, 6684, 496, 6441, 9134, 2390, 6682, 3713, 8215, 1126, 5977],
    "Commercial": [1441, 5543, 7266, 2838, 4094, 3752, 690, 4059, 9745, 9057, 2176],
    "Energy": [1380, 1318, 58, 2626, 2374, 1569, 7908, 2182, 7088, 8167, 6616],
    "Forestry": [698, 5893, 6233, 7113, 7876, 1651, 1909, 2298, 7788, 9182, 2887],
    "Industrial": [481, 3259, 1332, 9628, 8433, 2278, 3356, 7441, 430, 5237, 5262],
    "Marine": [5706, 9511, 1578, 2326, 9668, 7962, 5831, 7882, 5570, 6672, 5534],
    "Residential": [4112, 1224, 440, 4447, 9649, 7338, 6839, 9791, 3082, 9235, 1349],
    "Transportation": [9558, 1090, 1208, 7064, 4669, 8791, 547, 4198, 4728, 8260, 2205],
    "Waste": [4961, 5922, 2939, 9404, 9790, 6139, 5499, 7832, 1205, 5028, 8280]
}

# Calculate total emissions and offsets for each year
total_emissions = {}
total_offsets = {}

for sector in emissions_data:
    for year in range(2013, 2024):
        if year not in total_emissions:
            total_emissions[year] = 0
            total_offsets[year] = 0
        total_emissions[year] += emissions_data[sector][year - 2013]
        total_offsets[year] += offset_data[sector][year - 2013]

# JSON object 
output = {}

for year in total_emissions:
    output[year] = {
        "Emission": total_emissions[year],
        "Offset": total_offsets[year]
    }

# Convert to JSON format
json_output = json.dumps(output, indent=4)

# Print or save the JSON output
print(json_output)

with open('emission_offset_data.json', 'w') as json_file:
    json.dump(output, json_file, indent=4)
