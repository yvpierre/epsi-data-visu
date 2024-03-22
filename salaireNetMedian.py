import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
path = "excelFiles/insertion_professionnelle-master_donnees_nationales.csv"
try:
    df = pd.read_csv(path, sep=';', encoding='utf-8')

    # Remplacer les valeurs 'ns' et 'nd' par NaN
    df.replace(['ns', 'nd'], np.nan, inplace=True)

    # Convertir la colonne de salaire en float et supprimer les lignes avec des valeurs manquantes
    df['salaire_net_median_des_emplois_a_temps_plein'] = pd.to_numeric(df['salaire_net_median_des_emplois_a_temps_plein'], errors='coerce')
    df.dropna(subset=['salaire_net_median_des_emplois_a_temps_plein'], inplace=True)

    # Trier les données par année
    df.sort_values(by='annee', ascending=True, inplace=True)

    # Calculer la médiane du salaire net pour chaque année
    median_salaire_par_an = df.groupby('annee')['salaire_net_median_des_emplois_a_temps_plein'].median()

    # Créer un graphique linéaire pour afficher l'évolution du salaire net médian au fil des ans
    plt.figure(figsize=(10, 6))
    plt.plot(median_salaire_par_an.index, median_salaire_par_an.values, marker='o', linestyle='-')
    plt.title('Évolution du Salaire Net Médian en Fonction des Années')
    plt.xlabel('Année')
    plt.ylabel('Salaire Net Médian')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Error: File not found at {path}")
