import pandas as pd
import os

# combine the different csv files into a DataFrame

directory = r'C:\Users\99gio\OneDrive\Desktop\prove python\dati 2000-2022'

dataframes = []

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    df = pd.read_csv(filepath)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)


#starting to adjust the dataframe by viewing and selecting only the columns and raws i consider relevant

unique_stages = combined_df['Stage'].unique()

combined_df = combined_df[combined_df['Stage'] != 'Qualifying']

combined_df = combined_df.drop(columns=['Stage','Round','Group','Date', 'Comments', '∑FT','ET','P'])

combined_df['Team 1'] = combined_df['Team 1'].str.extract(r'^([^›]+)')
combined_df['Team 2'] = combined_df['Team 2'].str.extract(r'^([^›]+)')

unique_teams = combined_df['Team 1'].unique()