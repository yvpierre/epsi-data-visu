import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

excel_file_path = './excelFiles/indicateurs_nationaux_apprentissage_2020_2021.xlsx'

df_niveau_specialite = pd.read_excel(excel_file_path, sheet_name='Par niveau et spécialité')
df_prepared = df_niveau_specialite.iloc[2:].copy()
df_prepared.columns = df_niveau_specialite.iloc[1]

df_prepared = df_prepared[~df_prepared['Niveau de formation (regroupé)'].str.contains("ensemble", case=False, na=False)]

columns_to_convert = ['dont : CDI', 'dont : CDD', 'dont : Intérim', 'dont : Contrat pro', 'dont : Autres']
for column in columns_to_convert:
    df_prepared[column] = pd.to_numeric(df_prepared[column], errors='coerce').fillna(0).astype(float)

grouped = df_prepared.groupby('Niveau de formation (regroupé)').agg({
    'dont : CDI': 'sum',
    'dont : CDD': 'sum',
    'dont : Intérim': 'sum',
    'dont : Contrat pro': 'sum',
    'dont : Autres': 'sum'
}).reset_index()

grouped.columns = ['Niveau de Formation', 'CDI', 'CDD', 'Intérim', 'Contrat Pro', 'Autres']

category_totals = grouped[['CDI', 'CDD', 'Intérim', 'Contrat Pro', 'Autres']].sum(axis=1)
grouped_prop = grouped[['CDI', 'CDD', 'Intérim', 'Contrat Pro', 'Autres']].div(category_totals, axis=0)

category_names = ['CDI', 'CDD', 'Intérim', 'Contrat Pro', 'Autres']
labels = grouped['Niveau de Formation']
data = grouped_prop.to_numpy()

fig, ax = plt.subplots(figsize=(10, 8))

category_colors = plt.get_cmap('RdYlGn')(np.linspace(0.15, 0.85, len(category_names)))

start = np.zeros(len(labels))

for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    widths = data[:, i]
    ax.barh(labels, widths, left=start, label=colname, color=color)
    start = start + widths

ax.invert_xaxis()

ax.set_xlabel('Proportion')
ax.set_title('Répartition des types de contrats par niveau de formation')
ax.legend(
    ncol=len(category_names), 
    bbox_to_anchor=(0, -0.1),
    loc='upper left', 
    fontsize='small'
)

plt.show()
