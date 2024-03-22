import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
path = "excelFiles/insertion_professionnelle-master_donnees_nationales.csv"
try:
    df = pd.read_csv(path, sep=';', encoding='utf-8')

    # Remplacer les valeurs 'ns' et 'nd' par NaN
    df.replace(['ns', 'nd'], np.nan, inplace=True)

    # Convertir la colonne de pourcentage en float et supprimer les lignes avec des valeurs manquantes
    df['emplois_stables'] = pd.to_numeric(df['emplois_stables'], errors='coerce')
    df.dropna(subset=['emplois_stables'], inplace=True)

    # Grouper les données par domaine et par genre et calculer la moyenne du pourcentage des emplois stables
    grouped_data = df.groupby(['domaine', 'genre'])['emplois_stables'].mean().unstack()

    # Créer un graphique à barres groupées avec des couleurs modifiées
    colors = ['#4575b4', '#fee090', '#d73027']  # Deux nuances de bleu et orange
    ax = grouped_data.plot(kind='barh', stacked=False, figsize=(12, 8), color=colors)

    # Ajouter des labels et une légende
    plt.title('Pourcentage des Emplois Stables par Domaine et par Genre')
    plt.ylabel('Domaine')
    plt.xlabel('Pourcentage des Emplois Stables')
    plt.legend(title='Genre', loc='lower right')

    # Afficher le graphique
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Error: File not found at {path}")
