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

combined_df = combined_df.drop(columns=['Stage','Round','Group', 'Comments', '∑FT','ET','P'])

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

Teams_nd_Stadiums_df = pd.merge(combined_df, Stadiums_df[['Team', 'Stadium', 'City', 'Capacity']], left_on='Team 1', right_on='Team', how='left').drop(columns=['Team'])
print(Teams_nd_Stadiums_df.head())



# adding ranking to each team
ranking_files = [
    r'C:\Users\99gio\OneDrive\Desktop\prove python\RATINGS\rating 99_00.xlsx',
    r'C:\Users\99gio\OneDrive\Desktop\prove python\RATINGS\rating 00_01 04_05.xlsx',
    r'C:\Users\99gio\OneDrive\Desktop\prove python\RATINGS\rating 05_06 09_10.xlsx',
    r'C:\Users\99gio\OneDrive\Desktop\prove python\RATINGS\rating 10_11 14_15.xlsx'
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

all_ranking_melted = all_ranking.melt(id_vars=['Team'], var_name='Season', value_name='Rank')
all_ranking_melted.to_excel('unified_ranking_data2.xlsx', index=False)

print(all_ranking_melted.head())



# adding cities and ranking to the combined_df
team_to_city = pd.Series(Stadiums_df['City'].values, index=Stadiums_df['Team']).to_dict()
Teams_nd_Stadiums_df['City 2'] = Teams_nd_Stadiums_df['Team 2'].map(team_to_city)
print(Teams_nd_Stadiums_df.head())

Teams_nd_Stadiums_df['Cleaned Date'] = Teams_nd_Stadiums_df['Date'].str.extract(r'(\d{1,2} \w{3} \d{4})')[0]
Teams_nd_Stadiums_df['Cleaned Date'] = Teams_nd_Stadiums_df['Cleaned Date'].str.replace(r'\s+', ' ', regex=True)
Teams_nd_Stadiums_df['Date'] = pd.to_datetime(Teams_nd_Stadiums_df['Cleaned Date'], format='%d %b %Y', errors='coerce')


def get_previous_season(date):
    year = date.year
    if date.month > 7:
        return f"{year-1}-{year}"
    else:
        return f"{year-2}-{year-1}"

Teams_nd_Stadiums_df['Previous Season'] = Teams_nd_Stadiums_df['Date'].apply(get_previous_season)

print(Teams_nd_Stadiums_df[['Date', 'Previous Season']].head())


Teams_nd_Stadiums_df = pd.merge(
    Teams_nd_Stadiums_df,
    all_ranking_melted[['Team', 'Season', 'Rank']],
    left_on=['Team 1', 'Previous Season'],
    right_on=['Team', 'Season'],
    how='left',
    suffixes=('', '_Team1')
)

Teams_nd_Stadiums_df.drop(columns=['Team', 'Season'], inplace=True)
Teams_nd_Stadiums_df.rename(columns={'Rank': 'Ranking Team 1'}, inplace=True)

Teams_nd_Stadiums_df = pd.merge(
    Teams_nd_Stadiums_df,
    all_ranking_melted[['Team', 'Season', 'Rank']],
    left_on=['Team 2', 'Previous Season'],
    right_on=['Team', 'Season'],
    how='left',
    suffixes=('', '_Team2')
)

Teams_nd_Stadiums_df.drop(columns=['Team', 'Season'], inplace=True)
Teams_nd_Stadiums_df.rename(columns={'Rank': 'Ranking Team 2'}, inplace=True)

print(Teams_nd_Stadiums_df.head())
Teams_nd_Stadiums_df.to_excel('the_final_df_maybe.xlsx', index=False)
print(Teams_nd_Stadiums_df.columns)


# attempt to calculate distance between cities
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from tqdm import tqdm
import os

# Setup geolocator
geolocator = Nominatim(user_agent="your_unique_user_agent")

def get_location(city):
    try:
        return geolocator.geocode(city)
    except Exception as e:
        print(f"Error geocoding {city}: {str(e)}")
        return None

def calculate_distance(city1, city2):
    loc1 = get_location(city1)
    loc2 = get_location(city2)
    if loc1 and loc2:
        return geodesic((loc1.latitude, loc1.longitude), (loc2.latitude, loc2.longitude)).km
    return None

# Load existing distances from a backup file if it exists
distance_df = pd.read_csv('distances_backup.csv') if os.path.exists('distances_backup.csv') else pd.DataFrame(columns=['City1', 'City2', 'Distance'])
distance_dict = {tuple(row): dist for row, dist in distance_df.set_index(['City1', 'City2'])['Distance'].items()}

# # Uncomment the following lines to re-enable distance calculations
# for index, row in tqdm(Teams_nd_Stadiums_df.iterrows(), total=Teams_nd_Stadiums_df.shape[0]):
#     city_pair = (row['City'], row['City 2'])
#     if city_pair not in distance_dict:
#         dist = calculate_distance(*city_pair)
#         distance_dict[city_pair] = dist
#         new_row = pd.DataFrame({'City1': [row['City']], 'City2': [row['City 2']], 'Distance': [dist]})
#         distance_df = pd.concat([distance_df, new_row], ignore_index=True)
#     distance_df.to_csv('distances_backup.csv', index=False)

# Convert distance dictionary back to DataFrame for merging
distance_df = pd.DataFrame(list(distance_dict.items()), columns=['City_Pair', 'Distance'])
distance_df[['City1', 'City2']] = pd.DataFrame(distance_df['City_Pair'].tolist(), index=distance_df.index)

missing_distances = distance_df['Distance'].isna().sum()
if missing_distances == 0:
    print(f"Number of empty values before in 'Distance': {missing_distances}. Good Job")
else:
    print(f"Number of empty values before in 'Distance': {missing_distances}. There are still missing values.")

#I've checked the csv file and 22 cities have no distances calculated, so i manually add them

new_distances = [
    ('Istanbul', 'Prague', 1846),
    ('Celtic', 'Barcelona', 2128),
    ('Eindhoven', 'Trondheim', 1770),
    ('Leverkusen', 'Kyiv', 1900),
    ('Barcelona', 'Udine', 1350),
    ('Athens', 'Udine', 1775),
    ('Sofia', 'Bremen', 1900),
    ('Hamburg', 'Porto', 2481),
    ('Barcelona', 'Glasgow', 2128),
    ('Lisbon', 'Kyiv', 4146),
    ('London', 'Piraeus', 3147),
    ('Celtic', 'Villarreal', 2405),
    ('Liverpool', 'Lyon', 1285),
    ('Lyon', 'Bordeaux', 554),
    ('Lyon', 'Lisbon', 1700),
    ('Zilina', 'Moscow', 1745),
    ('Saint Petersburg', 'Porto', 4388),
    ('Moscow', 'Lille', 2640),
    ('Farum', 'London', 1263),
    ('Basel', 'Gelsenkirchen', 560),
    ('Nicosia', 'Amsterdam', 3700),
    ('Wolfsburg', 'Madrid', 2125)
]

for city1, city2, dist in new_distances:
    mask = (distance_df['City1'] == city1) & (distance_df['City2'] == city2)
    if mask.any():
        distance_df.loc[mask, 'Distance'] = dist

distance_df['Distance'] = distance_df['Distance'].round(0).astype(int)
missing_distances = distance_df['Distance'].isna().sum()

if missing_distances == 0:
    print(f"Number of empty values now in 'Distance': {missing_distances}. Good Job")
else:
    print(f"Number of empty values now in 'Distance': {missing_distances}. There are still missing values.")

Teams_nd_Stadiums_df.rename(columns={'City': 'City1', 'City 2': 'City2'}, inplace=True)
Teams_nd_Stadiums_df = Teams_nd_Stadiums_df.merge(distance_df[['City1', 'City2', 'Distance']], on=['City1', 'City2'], how='left')

print(Teams_nd_Stadiums_df.columns)
new_order = ['Date', 'Team 1', 'Team 2','FT', 'HT', 'Stadium', 'Capacity','City1', 'City2', 'Distance', 'Ranking Team 1', 'Ranking Team 2','Cleaned Date', 'Previous Season']
Teams_nd_Stadiums_df = Teams_nd_Stadiums_df[new_order]
Teams_nd_Stadiums_df.to_excel(r'C:\Users\99gio\OneDrive\Desktop\prove python\final_df_maybe.xlsx', index=False)

Final_df = Teams_nd_Stadiums_df
#finally i have adjusted the whole dataframe
print(Final_df.head())