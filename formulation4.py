import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Charger le modèle centré sur le PP avec Melt en sortie
model_path = "recipe1_prediction_model_PP.pkl"
model = joblib.load(model_path)

# Interface Streamlit
st.title("Prédiction des Recettes de Polymères (PP uniquement)")
st.header("Entrez les propriétés du matériau :")

charge = st.number_input("Charge %", min_value=0.0, format="%.2f")
izod = st.number_input("Izod Ft-lb/in", min_value=0.0, format="%.2f")
traction = st.number_input("Traction (N)", min_value=0.0, format="%.2f")
flexion = st.number_input("Flexion (psi)", min_value=0.0, format="%.2f")

if st.button("Prédire la Recette"):
    # Construire le DataFrame d'entrée
    input_data = pd.DataFrame([[charge, izod, traction, flexion]],
                              columns=['Charge', 'Izod', 'Traction', 'Flexion'])
    
    # Faire la prédiction
    prediction = model.predict(input_data)
    
    # Ajuster les valeurs pour qu'elles totalisent 100% (sauf Melt)
    total = sum(prediction[0][1:])
    normalized_prediction = [round((x / total) * 100, 2) if i > 0 else round(x, 2) 
                             for i, x in enumerate(prediction[0])]
    
    # Organiser les résultats ajustés
    output = {
        "Melt": normalized_prediction[0],
        "PP Repro Extrudé": normalized_prediction[1],
        "Compatibilisant": normalized_prediction[2],
        "Fibre de verre": normalized_prediction[3]
    }
    
    # Affichage du résultat
    st.subheader("Composition de la Recette Prévue :")
    st.write(output)

# Instructions pour l'installation et l'exécution :
# 1. Installer Streamlit et les dépendances :
#    pip install streamlit numpy joblib pandas scikit-learn
# 2. Lancer l'application :
#    streamlit run <nom_du_fichier>.py
