import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import cm


valid_lines = []

path="excelFiles/insertion_professionnelle-master_donnees_nationales.csv"
try:
    df = pd.read_csv(path, sep=';', index_col=False, encoding='utf-8', nrows=1000, on_bad_lines='warn')

    df_cleaned = df.replace(['ns', 'nd'], np.nan)
    df_cleaned['salaire_net_median_des_emplois_a_temps_plein'] = pd.to_numeric(
        df_cleaned['salaire_net_median_des_emplois_a_temps_plein'], errors='coerce')
    df_cleaned.dropna(subset=['salaire_net_median_des_emplois_a_temps_plein'], inplace=True)

    # Trier les données par année
    df_cleaned.sort_values(by='annee', ascending=True, inplace=True)

    # Extraction des données nettoyées et triées
    salaire_clean = df_cleaned['salaire_net_median_des_emplois_a_temps_plein'].astype(float).values
    annee_clean = df_cleaned['annee'].astype(str).values

    # Création de la figure et des axes
    fig, ax = plt.subplots(figsize=(10, 6))

    # Création du bar chart avec gradient
    bars = ax.bar(annee_clean, salaire_clean, color='lightblue', label='Salaire Net Médian')

    # Ajout du gradient aux barres
    gradient = np.linspace(0, 1, len(bars))
    for bar, grad in zip(bars, gradient):
        bar.set_color(cm.Oranges(grad))  # Changement de la couleur à Orange pour plus de contraste

    # Ajout des étiquettes pour les axes x et y
    ax.set_xlabel('Année')
    ax.set_ylabel('Salaire Net Médian')

    # Ajout d'un titre au graphique
    ax.set_title('Évolution des Salaires Net Médian en Fonction des Années (Données nettoyées)')

    # Ajout de la légende
    ax.legend()

    # Facultatif : Ajout d'une grille pour une meilleure lisibilité
    ax.grid(True)

    # Enregistrement du graphique
    plt.show()
    #print(df.head())
except FileNotFoundError:
    print(f"Error: File not found at {path}")
