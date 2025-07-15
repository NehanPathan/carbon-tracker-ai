

---


```markdown
# 🌱 Personal Carbon Tracker (AI-powered)

A simple Python application that helps users track their daily carbon footprint and receive **personalized tips** powered by **Google Gemini LLM** — aligned with **UN SDG #13: Climate Action**.

---

## 🚀 Features

- ✅ Log daily activities: travel, food habits, AC usage
- 🔍 Calculate carbon footprint using verified emission factors
- 🤖 Get 3 personalized suggestions from Gemini AI to reduce emissions
- 🌐 Optional Streamlit interface for a clean web-based UI
- 📦 Lightweight and beginner-friendly project setup

---

## 📸 Demo

| Terminal Mode                            | Streamlit Mode (optional)            |
|-----------------------------------------|--------------------------------------|
| ![Console Output](screenshots/console.png) | ![Streamlit Output](screenshots/ui.png) |

---

## 🧠 Tech Stack

- **Python 3.12+**
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- `streamlit` *(optional, for UI)*
- `google-generativeai` SDK
- `json` for data loading

---

## 📊 Emission Factors Used

| Activity      | Emission Factor         |
|---------------|--------------------------|
| Car Travel    | 0.165 kg CO₂/km          |
| Bus Travel    | 0.087 kg CO₂/km          |
| Train Travel  | 0.040 kg CO₂/km          |
| Veg Meal      | 1.2 kg CO₂/meal          |
| Non-Veg Meal  | 3.7 kg CO₂/meal          |
| AC Usage      | 0.206 kg CO₂/hour        |

---

## 📂 Project Structure

```

carbon-tracker-ai/
│
├── main.py                 # Handles input, output, and Gemini response
├── emissions.py            # Calculates CO₂ emissions
├── prompts.py              # Creates input prompt for Gemini
├── data/
│   └── emission\_factors.json
├── requirements.txt
├── README.md
└── (optional) Streamlit version

````

---

## 🧪 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/carbon-tracker-ai.git
cd carbon-tracker-ai
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your Gemini API Key

Replace in `main.py`:

```python
genai.configure(api_key="YOUR_API_KEY")
```

### 4. Run the App (Console Mode)

```bash
python main.py
```

### (Optional) Run Streamlit App

```bash
python -m streamlit run main.py
```

---

## 📌 Example Gemini Prompt

```text
The user submitted the following raw activity data:
{inputs}

This results in the following carbon emissions breakdown (in kg CO₂e):
{breakdown}

Based on both of these, suggest 3 personalized tips to reduce their carbon footprint.
```

---

## 📈 Why This Project?

This app empowers people — especially youth and students — to:

* Understand their **daily environmental impact**
* Learn **how to reduce emissions**
* Contribute to **sustainability goals (SDG 13)**

Perfect for hackathons, student innovation fairs, and climate awareness drives.

---

## 🙏 Credits

Made with ❤️ by **Nehan Pathan**
[GEC Gandhinagar](https://gecg28.ac.in)

---
```
