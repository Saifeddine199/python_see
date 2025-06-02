import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_with_releases(csv_data, csv_releases):
    # Lire les données
    data = pd.read_csv(csv_data, parse_dates=[0])
    releases = pd.read_csv(csv_releases, parse_dates=[0])

    # On suppose :
    # - data.csv : 1ère colonne = dates, 2ème colonne = valeur
    # - releases.csv : 1ère colonne = dates, 2ème colonne = descriptif

    date_col_data = data.columns[0]
    value_col_data = data.columns[1]

    date_col_releases = releases.columns[0]
    desc_col_releases = releases.columns[1]

    # Trier les données par date
    data.sort_values(date_col_data, inplace=True)
    releases.sort_values(date_col_releases, inplace=True)

    # Tracer la courbe principale
    plt.figure(figsize=(12, 6))
    plt.plot(data[date_col_data], data[value_col_data], label='Valeur principale', marker='o')

    # Ajouter les annotations pour les releases
    for _, row in releases.iterrows():
        release_date = row[date_col_releases]
        release_desc = row[desc_col_releases]

        plt.axvline(x=release_date, color='red', linestyle='--', alpha=0.7)
        plt.text(release_date, 
                 plt.ylim()[1]*0.95, 
                 f"{release_date.strftime('%Y-%m-%d')}\n{release_desc}", 
                 rotation=90, 
                 verticalalignment='top', 
                 horizontalalignment='right', 
                 fontsize=9, 
                 color='red')

    # Mise en forme 
    plt.xlabel('Date')
    plt.ylabel('Valeur')
    plt.title('Courbe avec annotations de releases')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Afficher le graphique
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py data.csv releases.csv")
    else:
        plot_with_releases(sys.argv[1], sys.argv[2])
