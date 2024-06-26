import pandas as pd
import os


# combine the different csv files into a DataFrame

directory = r'C:\Users\99gio\OneDrive\Desktop\prove python\dati 2000-2016'

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
print(Teams_nd_Stadiums_df.head())



# adding ranking to each team
ranking_files = [
    r'C:\Users\99gio\OneDrive\Desktop\prove python\RATINGS\rating 00_01 04_05.xlsx',
    r'C:\Users\99gio\OneDrive\Desktop\prove python\RATINGS\rating 05_06 09_10.xlsx',
    r'C:\Users\99gio\OneDrive\Desktop\prove python\RATINGS\rating 10_11 14_15.xlsx',
    r'C:\Users\99gio\OneDrive\Desktop\prove python\RATINGS\rating 15_16.xlsx'
]
all_ranking = pd.DataFrame()

for file in ranking_files:
    df = pd.read_excel(file)
    df['Team'] = df['Team'].str.lower().str.strip()
    if all_ranking.empty:
        all_ranking = df
    else:
        all_ranking = pd.merge(all_ranking, df, on='Team', how='outer')


# checking if everytTeam in 'Teams_nd_Stadiums_df' has a corresponding entry in 'all_ranking'
unique_teams_in_stadiums = set(Teams_nd_Stadiums_df['Team 1'].unique())
unique_teams_in_ranking = set(all_ranking['Team'].unique())
non_matching_teams = unique_teams_in_stadiums - unique_teams_in_ranking
print("Teams in Teams_nd_Stadiums_df without a match in all_ranking:", non_matching_teams)


# manually changing every team name that doesn't match :D
name_changes = {
    'galatasaray': 'galatasaray i̇stanbul aş',
    'fc basel': 'basel',
    'maccabi tel-aviv': 'maccabi tel aviv',
    'tottenham hotspur': 'tottenham hotspur fc',
    'malmö ff': 'malmo ff',
    'celta de vigo': 'celta vigo',
    'dvsc debrecen': 'debreceni vsc',
    'fc københavn': 'kobenhavn',
    'sevilla': 'sevilla fc',
    'villarreal': 'villarreal cf',
    'standard liège': 'standard liege',
    'udinese': 'udinese calcio',
    'ludogorets razgrad': 'pfc ludogorets razgrad',
    'helsingborg if': 'helsingborgs if',
    'fk astana': 'astana',
    'sporting cp lisbon': 'sporting cp',
    'anderlecht': 'rsc anderlecht',
    'napoli': 'ssc napoli',
    'ajax': 'afc ajax',
    'fenerbahçe': 'fenerbahçe i̇stanbul sk',
    'valencia': 'valencia cf',
    'boavista': 'boavista fc',
    'borussia mönchengladbach': 'borussia monchengladbach',
    'bayer leverkusen': 'bayer 04 leverkusen',
    'montpellier': 'montpellier hsc',
    'aa gent': 'kaa gent',
    'cska moscow': 'cska moskva',
    'racing genk': 'krc genk',
    'hapoel tel-aviv': 'hapoel tel aviv',
    'apoel nicosia': 'apoel nikosia',
    'olympiakos piraeus': 'olympiacos',
    'arsenal': 'arsenal fc',
    'leeds united': 'leeds united fc',
    'panathinaikos': 'panathinaikos fc',
    'schalke 04': 'fc schalke 04',
    'fiorentina': 'acf fiorentina',
    'spartak moscow': 'spartak moskva',
    'besiktas': 'beşiktaş i̇stanbul jk',
    'heerenveen': 'sc heerenveen',
    'lazio': 'ss lazio',
    'atlético madrid': 'atletico madrid',
    'trabzonspor': 'trabzonspor aş',
    'celtic': 'celtic fc',
    'deportivo la coruña': 'deportivo la coruna',
    'fc thun': 'thun',
    'glasgow rangers': 'rangers fc',
    'aab aalborg': 'aalborg bk',
    'liverpool': 'liverpool fc',
    'manchester city': 'manchester city fc',
    'real madrid': 'real madrid cf',
    'sturm graz': 'sk sturm graz',
    'fc nordsjælland': 'nordsjaelland',
    'manchester united': 'manchester united fc',
    'málaga cf': 'malaga cf',
    'feyenoord': 'feyenoord rotterdam',
    'real mallorca': 'rcd mallorca',
    'fc twente enschede': 'fc twente',
    'lokomotiv moscow': 'lokomotiv moskva',
    'newcastle united': 'newcastle united fc',
    'chelsea': 'chelsea fc',
    'petrzalka bratislava': 'petrzalka akademia',
    'fc zürich': 'fc zurich',
    'benfica': 'sl benfica'
}

all_ranking['Team'] = all_ranking['Team'].replace(name_changes)

# checking again
unique_teams_in_stadiums = set(Teams_nd_Stadiums_df['Team 1'].unique())
unique_teams_in_ranking = set(all_ranking['Team'].unique())
non_matching_teams = unique_teams_in_stadiums - unique_teams_in_ranking
print("hope this is empty:", non_matching_teams)
if non_matching_teams==set():
    print("Good job")

all_ranking.to_excel('unified_ranking_data.xlsx', index=False)
print(all_ranking.head())
