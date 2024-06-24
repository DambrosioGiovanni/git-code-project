import pandas as pd
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Step 1: Read and Combine CSV Files
directory = r'C:\Users\99gio\OneDrive\Desktop\prove python\dati 2000-2022'
dataframes = []

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

# Step 2: Filter and Clean the Combined DataFrame
print(combined_df.columns)

unique_stages = combined_df['Stage'].unique()
print(unique_stages)

combined_df = combined_df[combined_df['Stage'] != 'Qualifying']
print(combined_df['Stage'].unique())

combined_df = combined_df.drop(columns=['Stage', 'Round', 'Group', 'Date', 'Comments', '∑FT', 'ET', 'P'])

combined_df['Team 1'] = combined_df['Team 1'].str.extract(r'^([^›]+)')
combined_df['Team 2'] = combined_df['Team 2'].str.extract(r'^([^›]+)')
print(combined_df)
unique_teams = combined_df['Team 1'].unique()
print(unique_teams)

# Step 3: Fuzzy Match Teams to Stadiums
# Load stadiums data
df_TeamAndStadium = pd.read_csv('stadium_data.csv')

import chardet
with open(r'C:\Users\99gio\OneDrive\Desktop\prove python\Stadiums Data\FootballStadiums.csv', 'rb') as f:
    result = chardet.detect(f.read())

stadiums_df = pd.read_csv(r'C:\Users\99gio\OneDrive\Desktop\prove python\Stadiums Data\FootballStadiums.csv', encoding=result['encoding'])
print(stadiums_df.columns)

stadiums_df = stadiums_df[stadiums_df['Confederation'] == 'UEFA']
stadiums_df = stadiums_df[['Stadium', 'City', 'HomeTeams', 'Capacity', 'Country']]
stadiums_df.columns = ['Stadium', 'City', 'Team 1', 'Capacity', 'Country']

# Function for fuzzy matching
def fuzzy_match_team(row, choices, scorer, threshold=90):
    match = process.extractOne(row['Team 1'], choices, scorer=scorer)
    if match and match[1] >= threshold:
        return match[0]
    else:
        return None

# Apply fuzzy matching to team names
team_choices = stadiums_df['Team 1'].unique()
combined_df['Matched Team 1'] = combined_df.apply(lambda row: fuzzy_match_team(row, team_choices, fuzz.ratio), axis=1)

print(combined_df[['Team 1', 'Matched Team 1']].head())

# Step 4: Merge DataFrames
# Merge based on matched team names
merged_stadiums = pd.merge(combined_df, stadiums_df, how='left', left_on='Matched Team 1', right_on='Team 1')

# Select desired columns
merged_stadiums = merged_stadiums[['Team 1_x', 'Team 2', 'Stadium', 'City', 'Capacity', 'Country']]

# Final cleanup and column renaming
merged_stadiums.columns = ['Team 1', 'Team 2', 'Stadium', 'City', 'Capacity', 'Country']

print(merged_stadiums.head())