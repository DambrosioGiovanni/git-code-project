import pandas as pd
import os

directory = r'C:\Users\99gio\OneDrive\Desktop\prove python\dati 2000-2022'

dataframes = []

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    df = pd.read_csv(filepath)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

print(combined_df.head())
