Formulation and Recipe Prediction for Polymers
📌 Description

This project provides a framework for formulating and predicting polymer recipes using machine learning models.
It includes multiple Python scripts and pre-trained models that can be used to:

Predict optimal polymer formulations.

Estimate melt and processing properties.

Support decision-making in polymer design and recycling contexts.

📂 Project Structure
├── encoder.pkl                       # Pre-trained encoder for categorical/feature encoding
├── formulation.py                    # Main script for recipe prediction
├── formulation2.py                   # Alternative formulation implementation
├── formulation3.py                   # Extended features for prediction
├── formulation4.py                   # Variant with advanced optimization
├── optimized_ml_model.pkl            # Optimized ML model for formulation
├── recipe1_prediction_model.pkl      # Recipe prediction model (baseline)
├── recipe1_prediction_model_PP.pkl   # Recipe model specific for polypropylene (PP)
├── recipe_prediction_model.pkl       # General recipe prediction model
├── recipe_prediction_model_PP.pkl    # PP-specific recipe model
├── recipe_prediction_model_melt.pkl  # Model trained for melt property prediction
├── requirements.txt                  # Python dependencies
└── README.md                         # Project documentation

⚙️ Installation

Clone the repository

git clone https://github.com/<username>/<repo_name>.git
cd <repo_name>


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install the dependencies

pip install -r requirements.txt

🚀 Usage
Run a formulation script
python formulation.py

Example: predict with a model
import pickle
import numpy as np

# Load the recipe prediction model
with open("recipe_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

# Example input (replace with dataset features)
X_sample = np.array([[0.45, 0.35, 0.20]])

# Predict recipe outcome
y_pred = model.predict(X_sample)
print("Predicted formulation:", y_pred)

📊 Models

optimized_ml_model.pkl → Fine-tuned ML model for polymer formulation.

recipe1_prediction_model.pkl → Baseline recipe prediction.

recipe_prediction_model_melt.pkl → Model optimized for melt property estimation.

PP-specific models → Dedicated models for polypropylene formulations.

🔬 Applications

Polymer recipe prediction (multi-component blends).

Melt property optimization for extrusion and injection molding.

Reverse design of polymer formulations to achieve target mechanical/thermal properties.

Support for industrial recycling workflows.

🖋️ Author

Developed by Oumayma Tajir as part of ongoing PhD research on AI for polymer formulation, prediction, and optimization at Université de Sherbrooke.
