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

print(combined_df.columns)

unique_stages = combined_df['Stage'].unique()
print(unique_stages)

combined_df = combined_df[combined_df['Stage'] != 'Qualifying']
print(combined_df['Stage'].unique())

combined_df = combined_df.drop(columns=['Stage','Round','Group','Date', 'Comments', '∑FT','ET','P'])

combined_df['Team 1'] = combined_df['Team 1'].str.extract(r'^([^›]+)')
combined_df['Team 2'] = combined_df['Team 2'].str.extract(r'^([^›]+)')
combined_df['Team 1'] = combined_df['Team 1'].str.lower().str.strip()
combined_df['Team 2'] = combined_df['Team 2'].str.lower().str.strip()
print(combined_df)
unique_teams = combined_df['Team 1'].unique()
print(unique_teams)


# adding stadiums

file_path = r'C:\Users\99gio\OneDrive\Desktop\prove python\stadium_data.xlsx'
Stadiums_df = pd.read_excel(file_path, engine='openpyxl')
Stadiums_df['Team'] = Stadiums_df['Team'].str.strip().str.lower()
print(Stadiums_df.head())


# checking if every team has a match in the Stadiums_Df

unique_teams_combined_df = set(combined_df['Team 1'].unique())
unique_teams_stadiums_df = set(Stadiums_df['Team'].unique())

non_matching_teams = unique_teams_combined_df - unique_teams_stadiums_df
print("Non matching teams in combined_df:", non_matching_teams)

non_matching_teams_stadiums = unique_teams_stadiums_df - unique_teams_combined_df
print("Non matching teams in Stadiums_df:", non_matching_teams_stadiums)

Teams_nd_Stadiums_df = pd.merge(combined_df, Stadiums_df[['Team', 'Stadium', 'City', 'Capacity']], left_on='Team 1', right_on='Team', how='left')

# Stampa il risultato per verificare
print(Teams_nd_Stadiums_df.head())