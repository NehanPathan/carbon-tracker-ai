# prompts.py

def generate_prompt(inputs, breakdown):
    return f"""
The user submitted the following raw activity data:
{inputs}

This results in the following carbon emissions breakdown (in kg CO₂e):
{breakdown}

Based on both of these, suggest 3 personalized, realistic, and practical tips to reduce their carbon footprint. Focus on the activities with the highest impact, and keep the language simple and friendly.
"""
