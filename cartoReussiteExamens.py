import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

valid_lines = []

path="excelFiles/carto_reussite_examens.csv"
try:
    df = pd.read_csv(path, sep=';', index_col=False, encoding='utf-8', nrows=1000, on_bad_lines='warn')


    grouped_data = df.groupby('type_du_diplome')['taux_de_reussite_total'].mean()
    grouped_data_sorted = grouped_data.sort_values(ascending=False)

    plt.figure(figsize=(10, 6))

    grouped_data_sorted.plot(kind='bar', color='skyblue')

    plt.ylim(0.80, 1)  

    plt.xlabel('Type de diplôme')
    plt.ylabel('Taux de réussite moyen')
    plt.title('Taux de réussite par type de diplôme')

    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout() 
    plt.show()

except FileNotFoundError:
    print(f"Error: File not found at {path}")