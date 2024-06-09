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

combined_df['Team 1'] = combined_df['Team 1'].str.extract(r'^([^>]+)')

print(combined_df)


# adding stadiums

import chardet
with open(r'C:\Users\99gio\OneDrive\Desktop\prove python\Stadiums Data\FootballStadiums.csv', 'rb') as f:
    result = chardet.detect(f.read())

stadiums_df = pd.read_csv(r'C:\Users\99gio\OneDrive\Desktop\prove python\Stadiums Data\FootballStadiums.csv', encoding=result['encoding'])
print(stadiums_df.columns)

stadiums_df = stadiums_df[stadiums_df['Confederation'] == 'UEFA']
stadiums_df = stadiums_df[['Stadium', 'City', 'HomeTeams', 'Capacity', 'Country']]
stadiums_df.columns = ['Stadium', 'City', 'Team 1', 'Capacity', 'Country']


#combining matches and stadiums

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Funzione per effettuare il merge fuzzy
def fuzzy_merge(df1, df2, key1, key2, threshold=70):
    s = df1[key1].apply(lambda x: process.extractOne(x, df2[key2], scorer=fuzz.partial_ratio, score_cutoff=threshold))
    df1['Matches'] = s.apply(lambda x: x[0] if x else None)
    
    # Unire i due DataFrame basandosi sulla nuova colonna 'Matches'
    merged = pd.merge(df1, df2, left_on='Matches', right_on=key2, how='left')
    
    # Rimuovere la colonna 'Matches' dal DataFrame risultante
    merged.drop('Matches', axis=1, inplace=True)
    
    return merged

# Esegui il fuzzy merge
merged_df = fuzzy_merge(combined_df, stadiums_df, 'Team 1', 'Team 1', threshold=60)

# Visualizza il DataFrame risultante
print(merged_df.head())




