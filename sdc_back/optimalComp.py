import pandas as pd

offset_providers_data = pd.DataFrame({
    'ProjectID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'Company Name': ['WindInnovations', 'AquaConserv', 'GigaHarvest', 'GeoPower', 'SolarDynamics', 'GigaConserv', 'AquaDynamics', 'GeoRenewables', 'AquaRenewables', 'SolarRenewables', 'SolarPower', 'AquaDynamics', 'BioDynamics', 'NeoTech', 'WindSystems', 'GreenSolutions', 'WindRenewables', 'EcoSystems', 'TerraSolutions', 'BioDynamics'],
    'Sector': ['Aviation', 'Forestry', 'Commercial', 'Energy', 'Residential', 'Commercial', 'Energy', 'Waste', 'Agriculture', 'Marine', 'Industrial', 'Marine', 'Industrial', 'Aviation', 'Energy', 'Residential', 'Agriculture', 'Waste', 'Transportation', 'Transportation'],
    'CO2OffsetTonnes': [6000, 3234, 3500, 5304, 8000, 6543, 7078, 6989, 4235, 7576, 5354, 7689, 6430, 5238, 3249, 5790, 3245, 6342, 4569, 7509],
    'Cost': [1343, 1545, 998, 850, 1300, 803, 1203, 932, 650, 2980, 1832, 3240, 3480, 2342, 3240, 4579, 1343, 4329, 870, 4239]
})

# empty dictionary to store the optimal providers
optimal_providers = {}

# group the data by sector
grouped_data = offset_providers_data.groupby('Sector')

# iterate through each sector
for sector, group in grouped_data:
    # sortthe providers by offset tons (descending) and cost (ascending)
    sorted_providers = group.sort_values(by=['CO2OffsetTonnes', 'Cost'], ascending=[False, True])
    
    # select the provider with the highest offset tons and lowest cost
    top_provider = sorted_providers.iloc[0]  # Select the first row (highest offset tons, lowest cost)
    
    # add the top provider to the optimal providers dictionary
    optimal_providers[sector] = top_provider['Company Name']

# printf
for sector, provider in optimal_providers.items():
    print(f"For the {sector} sector, the optimal provider is: {provider}.")
