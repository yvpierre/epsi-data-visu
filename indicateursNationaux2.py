import pandas as pd
import matplotlib.pyplot as plt

# Chemin du fichier Excel
excel_file_path = './excelFiles/indicateurs_nationaux_apprentissage_2020_2021.xlsx'

# Chargement des données
df = pd.read_excel(excel_file_path, sheet_name='Par niveau et spécialité')

# Suppression des premières lignes et définition de la nouvelle entête
df.columns = df.iloc[1] # Définit la deuxième ligne comme entête
df = df.drop(index=[0, 1]) # Supprime les deux premières lignes qui ne sont plus nécessaires

# Renommage des colonnes pour clarifier
df.rename(columns={
    "Spécialité": "Specialite",
    "Part en poursuite d'études (c)=(2)/(1)": "Part_en_poursuite_etudes",
    "Part en emploi 6 mois après la sortie (d)=(4)/(1)": "Part_en_emploi",
    "Part des autres situations (e)=100-(c)-(d)": "Part_autres_situations"
}, inplace=True)

# Sélection des colonnes d'intérêt
df = df[["Specialite", "Part_en_poursuite_etudes", "Part_en_emploi", "Part_autres_situations"]]

# Conversion des colonnes de pourcentage en numérique
df[["Part_en_poursuite_etudes", "Part_en_emploi", "Part_autres_situations"]] = df[["Part_en_poursuite_etudes", "Part_en_emploi", "Part_autres_situations"]].apply(pd.to_numeric)

# Regroupement par spécialité et calcul de la moyenne des pourcentages
df_grouped = df.groupby('Specialite').mean().reset_index()

# Tri des données pour une meilleure lisibilité sur le graphique
df_grouped.sort_values(by='Part_en_poursuite_etudes', ascending=True, inplace=True)

# Création du graphique
plt.figure(figsize=(10, 8))
# Barres pour la part en poursuite d'études
plt.barh(df_grouped['Specialite'], df_grouped['Part_en_poursuite_etudes'], label='Poursuite d\'études')
# Barres pour la part en emploi, décalées à droite par les valeurs de la poursuite d'études
plt.barh(df_grouped['Specialite'], df_grouped['Part_en_emploi'], left=df_grouped['Part_en_poursuite_etudes'], label='Emploi après 6 mois')
# Barres pour les autres situations, décalées à droite par la somme des valeurs précédentes
plt.barh(df_grouped['Specialite'], df_grouped['Part_autres_situations'], left=df_grouped['Part_en_poursuite_etudes']+df_grouped['Part_en_emploi'], label='Autres situations')

plt.xlabel('Pourcentage')
plt.ylabel('Spécialité')
plt.title('Répartition des situations des diplômés par spécialité')
plt.legend()

plt.tight_layout()
plt.show()

