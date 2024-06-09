import pandas as pd
import os

# combine the different csv files into 1 DataFrame

directory = r'C:\Users\99gio\OneDrive\Desktop\prove python\dati 2000-2022'

dataframes = []

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    df = pd.read_csv(filepath)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

#starting to adjust the dataframe by viewing and selecting the columns and raws i consider not relevant

print(combined_df.columns)

unique_stages = combined_df['Stage'].unique()
print(unique_stages)

combined_df = combined_df[combined_df['Stage'] != 'Qualifying']
print(combined_df['Stage'].unique())

combined_df = combined_df.drop(columns=['Stage','Round','Group','Date', 'Comments', '∑FT','ET','P'])
print(combined_df)