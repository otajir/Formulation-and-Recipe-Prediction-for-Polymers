import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Charger le modèle et l'encoder
model = joblib.load("optimized_ml_model.pkl")
encoder = joblib.load("encoder.pkl")


# Interface Streamlit
st.title("Prédiction du PP convenable pour ses propriétés")

st.header("Entrez les valeurs des caractéristiques :")

flex = st.number_input("Flexion", min_value=0.0, format="%.2f")
traction = st.number_input("Traction", min_value=0.0, format="%.2f")
cendre = st.number_input("Cendre", min_value=0.0, format="%.2f")
I48 = st.number_input("I48", min_value=0.0, format="%.2f")

if st.button("Prédire"):
    # Assurez-vous que l'entrée est un DataFrame avec les bonnes colonnes
    input_data = pd.DataFrame([[flex, traction, cendre, I48]], columns=['flex', 'traction', 'cendre', 'I48'])
    prediction = model.predict(input_data)
    
    # Extraire la partie numérique et les catégories encodées
    melt_pred = prediction[0][0]  # Valeur numérique
    categorical_pred = prediction[0][1:]  # Valeurs encodées (OneHot)
    
    # Décoder les catégories prédictes
    decoded_categories = encoder.inverse_transform([categorical_pred])[0]
    
    # Associer les résultats aux bonnes variables
    output = {
        "Items": decoded_categories[0],  # Nom de l'item
        "Melt": round(melt_pred, 2),  # Valeur numérique arrondie
        "COULEUR": decoded_categories[1],  # Couleur catégorique
        "I_CM": decoded_categories[2],  # Catégorie I_CM
        "I_G": decoded_categories[3],  # Catégorie I_G
        "I_F": decoded_categories[4]   # Catégorie I_F
    }
    
    # Affichage du résultat
    st.subheader("Résultat de la Prédiction :")
    st.write(output)
    
    # Graphique de précision du modèle
    #st.subheader("Évaluation du modèle")
    
    # Génération de valeurs aléatoires pour comparaison (à remplacer par de vraies valeurs de test)
   # y_true = np.random.uniform(melt_pred - 0.5, melt_pred + 0.5, 10)
    # y_pred = [melt_pred] * 10
    
    # Calcul de l'erreur
    # mae = mean_absolute_error(y_true, y_pred)
    # mse = mean_squared_error(y_true, y_pred)
    
    # fig, ax = plt.subplots()
    # ax.scatter(y_true, y_pred, label="Prédictions vs Réel")
   # ax.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], 'r--', label="Parfaite Prédiction")
    # ax.set_xlabel("Valeurs réelles")
    # ax.set_ylabel("Valeurs prédites")
    # ax.legend()
   #  st.pyplot(fig)
    
   #  st.write(f"Erreur absolue moyenne (MAE) : {round(mae, 3)}")
    # st.write(f"Erreur quadratique moyenne (MSE) : {round(mse, 3)}")

# Instructions pour l'installation et l'exécution :
# 1. Installer Streamlit et les dépendances :
#    pip install streamlit numpy joblib pandas scikit-learn matplotlib
# 2. Lancer l'application :
#    streamlit run <nom_du_fichier>.py
