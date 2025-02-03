import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Charger le modèle centré sur le PP avec Melt en sortie
model_path = "recipe_prediction_model_melt.pkl"
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
    # Faire la prédiction

    # Vérifier si prediction est un tableau numpy ou une liste
    if isinstance(prediction, np.ndarray) and prediction.ndim == 2:
        melt_pred = round(prediction[0, 0], 2)
    elif isinstance(prediction, np.ndarray) and prediction.ndim == 1:
        melt_pred = round(prediction[0], 2)
    else:
        melt_pred = round(float(prediction), 2)

    # Organiser les résultats ajustés
    output = {
        "Melt": melt_pred,
        "PP Repro Extrudé": 100.0  # Toujours 100%
}
    
#     # Organiser les résultats ajustés
#     output = {
#         "Melt": round(prediction[0][0], 2),
#         "PP Repro Extrudé": 100.0  # Toujours 100%
#     }
    
    # Affichage du résultat
    st.subheader("Composition de la Recette Prévue :")
    st.write(output)

# # Instructions pour l'installation et l'exécution :
# 1. Installer Streamlit et les dépendances :
#    pip install streamlit numpy joblib pandas scikit-learn
# 2. Lancer l'application :
#    streamlit run <nom_du_fichier>.py
