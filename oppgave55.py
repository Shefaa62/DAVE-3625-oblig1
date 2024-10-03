import pandas as pd
import os

# Sjekk nåværende arbeidskatalog og liste over filer i denne katalogen
print("Nåværende arbeidskatalog:", os.getcwd())
print("Filer i denne katalogen:", os.listdir())

# Prøv å lese inn datasettet
try:
    # Sørg for at filbanen til Grocery_dataset.csv er korrekt
    df = pd.read_csv('Grocery_dataset.csv')  # Endre banen hvis nødvendig
    print("Datasettet ble lastet inn riktig.")
except FileNotFoundError:
    print("Filen 'Grocery_dataset.csv' ble ikke funnet. Vennligst sjekk filbanen.")

# Hvis datasettet er lastet inn, fortsett med oppgaven
if 'df' in locals():  # Sjekk om df eksisterer
    # Vis de første radene for å bekrefte at datasettet ble lastet inn
    print("De første radene i datasettet:")
    print(df.head())

    # Oppgave 5: Fjern kolonnene med indeksverdier 0 og 6 og opprett en ny DataFrame
    columns_to_drop = [0, 6]
    Grc_new_df = df.drop(df.columns[columns_to_drop], axis=1)

    # Skriv ut de første radene for å bekrefte at kolonnene er fjernet
    print("\nGrc_new_df after dropping columns with index 0 and 6:")
    print(Grc_new_df.head())

    # Oppgave 6: Lag to forskjellige DataFrames basert på Outlet_Type
    SupType_1 = Grc_new_df[Grc_new_df['Outlet_Type'] == 'Supermarket Type1']
    SupType_2 = Grc_new_df[Grc_new_df['Outlet_Type'] == 'Supermarket Type2']

    # Skriv ut de første radene for hver DataFrame for å bekrefte
    print("\nSupType_1 DataFrame:")
    print(SupType_1.head())

    print("\nSupType_2 DataFrame:")
    print(SupType_2.head())
else:
    print("Kjøring av koden ble stoppet fordi datasettet ikke ble funnet.")
