import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Charger le modèle centré sur le PP
model_path = "recipe_prediction_model_PP.pkl"
model = joblib.load(model_path)

# Interface Streamlit
st.title("Prédiction des Recettes de Polymères (PP uniquement)")

st.header("Entrez les propriétés du matériau :")

melt = st.number_input("Melt (230°C 2.16 kg)", min_value=0.0, format="%.2f")
charge = st.number_input("Charge %", min_value=0.0, format="%.2f")
izod = st.number_input("Izod Ft-lb/in", min_value=0.0, format="%.2f")
traction = st.number_input("Traction (N)", min_value=0.0, format="%.2f")
flexion = st.number_input("Flexion (psi)", min_value=0.0, format="%.2f")

if st.button("Prédire la Recette"):
    # Construire le DataFrame d'entrée
    input_data = pd.DataFrame([[melt, charge, izod, traction, flexion]],
                              columns=['Melt', 'Charge', 'Izod', 'Traction', 'Flexion'])
    
    # Faire la prédiction
    prediction = model.predict(input_data)
    
    # Ajuster les valeurs pour qu'elles totalisent 100%
    total = sum(prediction[0])
    normalized_prediction = [round((x / total) * 100, 2) for x in prediction[0]]
    
    # Organiser les résultats ajustés
    output = {
        "PP Repro Extrudé": normalized_prediction[0],
        "Compatibilisant": normalized_prediction[1],
        "Fibre de verre": normalized_prediction[2]
    }
    
    # Affichage du résultat
    st.subheader("Composition de la Recette Prévue :")
    st.write(output)

# Instructions pour l'installation et l'exécution :
# 1. Installer Streamlit et les dépendances :
#    pip install streamlit numpy joblib pandas scikit-learn
# 2. Lancer l'application :
#    streamlit run <nom_du_fichier>.py
