import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from Excel file
excel_file = './excelFiles/indicateurs_nationaux_apprentissage_2020_2021.xlsx'
df = pd.read_excel(excel_file, sheet_name="Par niveau et spécialité")

# Specify the column indexes you want for the X-axis and different types of answers
x_axis_index = 1
answer_indexes = [9, 10, 11, 12, 13]

# Extract data for X-axis (questions) and different types of answers
questions = [str(q) for q in df.iloc[:, x_axis_index].tolist()]
answers_data = df.iloc[:, answer_indexes].values.T  # Transpose to have answers as rows

def survey(questions, answers_data):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)

    category_colors = plt.cm.RdYlGn(np.linspace(0.15, 0.85, len(answer_indexes)))

    data_cum = np.zeros_like(answers_data[0])

    for i, (answer_index, color) in enumerate(zip(answer_indexes, category_colors)):
        widths = answers_data[i]
        starts = data_cum
        rects = ax.barh(questions, widths, left=starts, height=0.5,
                        label=f"Answer {answer_index}", color=color)

        data_cum += widths

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, labels=[f'{width:.2f}' for width in widths], label_type='center', color=text_color)

    ax.legend(bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
    plt.show()

survey(questions, answers_data)
