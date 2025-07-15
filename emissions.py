
# emissions.py
import json

# Load emission factors from a JSON file
def load_emission_factors(path='data/emission_factors.json'):
    with open(path, 'r') as f:
        return json.load(f)

# Calculate total carbon footprint based on user input
def calculate_footprint(inputs, factors):
    total = 0
    details = {}
    for key in inputs:
        emission = inputs[key] * factors.get(key, 0)
        details[key] = round(emission, 2)
        total += emission
    return round(total, 2), details
