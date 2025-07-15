import streamlit as st
from emissions import load_emission_factors, calculate_footprint
from prompts import generate_prompt
import google.generativeai as genai

# Set up Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("models/gemini-1.5-flash")

# UI with white space
st.title("🌱 Personal Carbon Tracker")
st.markdown("Enter your daily activity to calculate your carbon footprint.")

car = st.number_input("Km travelled by car", min_value=0.0, step=1.0)
bus = st.number_input("Km travelled by bus", min_value=0.0, step=1.0)
train = st.number_input("Km travelled by train", min_value=0.0, step=1.0)
veg_meal = st.number_input("Number of veg meals", min_value=0, step=1)
nonveg_meal = st.number_input("Number of non-veg meals", min_value=0, step=1)
ac_hour = st.number_input("Hours of AC usage", min_value=0.0, step=0.5)

if st.button("Calculate My Emissions"):
    inputs = {
        "car": car,
        "bus": bus,
        "train": train,
        "veg_meal": veg_meal,
        "nonveg_meal": nonveg_meal,
        "ac_hour": ac_hour
    }

    factors = load_emission_factors()
    total_emission, breakdown = calculate_footprint(inputs, factors)

    st.subheader("📊 Carbon Emission Summary")
    for k, v in breakdown.items():
        st.write(f"**{k}**: {v} kg CO₂e")
    st.markdown(f"### 🌍 Total Emission: `{total_emission} kg CO₂e`")

    # Gemini tips
    prompt = generate_prompt(inputs, breakdown)
    response = model.generate_content(prompt)

    st.subheader("🌿 Gemini's Carbon Reduction Tips")
    st.markdown(response.text)
