import pandas as pd

# Dati sugli stadi
stadium_data = {
    'Team': [
        'Sporting CP', 'Spartak Moskva', 'Sparta Praha', 'Shakhtar Donetsk', 'Valencia CF', 'Olympique Lyon',
        'Rangers FC', 'Galatasaray İstanbul AŞ', 'Hamburger SV', 'Panathinaikos FC', 'Helsingborgs IF', 'Rosenborg BK',
        'PSV Eindhoven', 'Manchester United FC', 'AC Milan', 'FC Barcelona', 'Deportivo La Coruna', 'Juventus',
        'Bayern München', 'Paris Saint-Germain', 'Dinamo Kiev', 'RSC Anderlecht', 'Leeds United FC', 'Beşiktaş İstanbul JK',
        'Bayer 04 Leverkusen', 'Real Madrid CF', 'SS Lazio', 'Arsenal FC', 'sc Heerenveen', 'Olympiacos',
        'SK Sturm Graz', 'AS Monaco', 'Lokomotiv Moskva', 'AS Roma', 'Liverpool FC', 'RCD Mallorca', 'FC Schalke 04',
        'FC Nantes', 'Fenerbahçe İstanbul SK', 'Borussia Dortmund', 'Boavista FC', 'Celtic FC', 'Lille OSC', 'FC Porto',
        'Feyenoord Rotterdam', 'AJ Auxerre', 'Basel', 'KRC Genk', 'AFC Ajax', 'Newcastle United FC', 'Maccabi Haifa',
        'RC Lens', 'Club Brugge', 'AEK Athens', 'Internazionale', 'Partizan Belgrade', 'Real Sociedad', 'VfB Stuttgart',
        'Olympique Marseille', 'Chelsea FC', 'Celta Vigo', 'Maccabi Tel Aviv', 'Werder Bremen', 'CSKA Moskva',
        'Real Betis', 'Petrzalka Akademia', 'Rapid Wien', 'Udinese Calcio', 'SL Benfica', 'Villarreal CF', 'Thun',
        'Kobenhavn', 'Steaua Bucuresti', 'Levski Sofia', 'Girondins Bordeaux', 'Slavia Praha', 'Sevilla FC', 'Aalborg BK',
        'ACF Fiorentina', 'BATE Borisov', 'Zenit St. Petersburg', 'CFR Cluj', 'Anorthosis Famagusta', 'Atletico Madrid',
        'VfL Wolfsburg', 'FC Zurich', 'Standard Liege', 'Debreceni VSC', 'Rubin Kazan', 'Unirea Urziceni', 'AZ Alkmaar',
        'APOEL Nikosia', 'FC Twente', 'Bursaspor', 'MSK Zilina', 'Sporting Braga', 'Tottenham Hotspur FC',
        'Hapoel Tel Aviv', 'Viktoria Plzen', 'Manchester City FC', 'Dinamo Zagreb', 'SSC Napoli', 'Trabzonspor AŞ',
        'Otelul Galati', 'Montpellier HSC', 'Malaga CF', 'Nordsjaelland', 'Austria Wien', 'NK Maribor', 'Athletic Bilbao',
        'Malmo FF', 'PFC Ludogorets Razgrad', 'KAA Gent', 'Astana', 'Borussia Monchengladbach'
    ],
    'Stadium': [
        'Estádio José Alvalade', 'Otkritie Arena', 'Generali Arena', 'Donbass Arena', 'Mestalla', 'Groupama Stadium',
        'Ibrox Stadium', 'Türk Telekom Stadium', 'Volksparkstadion', 'OAKA Stadium', 'Olympia', 'Lerkendal Stadion',
        'Philips Stadion', 'Old Trafford', 'San Siro', 'Camp Nou', 'Abanca-Riazor', 'Allianz Stadium', 'Allianz Arena',
        'Parc des Princes', 'NSC Olimpiyskiy', 'Constant Vanden Stock', 'Elland Road', 'Vodafone Park',
        'BayArena', 'Santiago Bernabéu', 'Stadio Olimpico', 'Emirates Stadium', 'Abe Lenstra Stadion', 'Karaiskakis Stadium',
        'Merkur Arena', 'Stade Louis II', 'RZD Arena', 'Stadio Olimpico', 'Anfield', 'Son Moix', 'Veltins-Arena',
        'Stade de la Beaujoire', 'Şükrü Saracoğlu Stadium', 'Signal Iduna Park', 'Estádio do Bessa', 'Celtic Park',
        'Stade Pierre-Mauroy', 'Estádio do Dragão', 'De Kuip', 'Stade de l\'Abbé-Deschamps', 'St. Jakob-Park',
        'Luminus Arena', 'Johan Cruijff ArenA', 'St James\' Park', 'Sammy Ofer Stadium', 'Stade Bollaert-Delelis',
        'Jan Breydel Stadium', 'Olympic Stadium', 'San Siro', 'Partizan Stadium', 'Anoeta', 'Mercedes-Benz Arena',
        'Stade Vélodrome', 'Stamford Bridge', 'Balaídos', 'Bloomfield Stadium', 'Weserstadion', 'VEB Arena',
        'Benito Villamarín', 'Štadión Pasienky', 'Allianz Stadion', 'Dacia Arena', 'Estádio da Luz', 'Estadio de la Cerámica',
        'Stockhorn Arena', 'Parken Stadium', 'Arena Națională', 'Georgi Asparuhov', 'Matmut Atlantique', 'Eden Arena',
        'Ramón Sánchez Pizjuán', 'Aalborg Portland Park', 'Stadio Artemio Franchi', 'Borisov Arena', 'Gazprom Arena',
        'Stadionul Dr. Constantin Rădulescu', 'Antonis Papadopoulos Stadium', 'Wanda Metropolitano', 'Volkswagen Arena',
        'Letzigrund', 'Stade Maurice Dufrasne', 'Nagyerdei Stadion', 'Kazan Arena', 'Stadionul Tineretului',
        'AFAS Stadion', 'GSP Stadium', 'De Grolsch Veste', 'Bursa Büyükşehir Belediye', 'Štadión Pod Dubňom',
        'Estádio Municipal de Braga', 'Tottenham Hotspur Stadium', 'Bloomfield Stadium', 'Doosan Arena', 'Etihad Stadium',
        'Stadion Maksimir', 'Stadio Diego Armando Maradona', 'Şenol Güneş Stadium', 'Stadionul Oțelul', 'Stade de la Mosson',
        'La Rosaleda', 'Right to Dream Park', 'Generali Arena', 'Ljudski vrt', 'San Mamés', 'Eleda Stadion',
        'Huvepharma Arena', 'Ghelamco Arena', 'Astana Arena', 'Borussia-Park'
    ],
    'City': [
        'Lisbon', 'Moscow', 'Prague', 'Donetsk', 'Valencia', 'Lyon', 'Glasgow', 'Istanbul', 'Hamburg', 'Athens',
        'Helsingborg', 'Trondheim', 'Eindhoven', 'Manchester', 'Milan', 'Barcelona', 'A Coruña', 'Turin', 'Munich', 'Paris',
        'Kyiv', 'Anderlecht', 'Leeds', 'Istanbul', 'Leverkusen', 'Madrid', 'Rome', 'London', 'Heerenveen', 'Piraeus',
        'Graz', 'Monaco', 'Moscow', 'Rome', 'Liverpool', 'Palma', 'Gelsenkirchen', 'Nantes', 'Istanbul', 'Dortmund',
        'Porto', 'Celtic', 'Lille', 'Porto', 'Rotterdam', 'Auxerre', 'Basel', 'Genk', 'Amsterdam', 'Newcastle',
        'Haifa', 'Lens', 'Bruges', 'Athens', 'Milan', 'Belgrade', 'San Sebastian', 'Stuttgart', 'Marseille', 'London',
        'Vigo', 'Tel Aviv', 'Bremen', 'Moscow', 'Seville', 'Bratislava', 'Vienna', 'Udine', 'Lisbon', 'Villarreal',
        'Thun', 'Copenhagen', 'Bucharest', 'Sofia', 'Bordeaux', 'Prague', 'Seville', 'Aalborg', 'Florence',
        'Borisov', 'Saint Petersburg', 'Cluj-Napoca', 'Larnaca', 'Madrid', 'Wolfsburg', 'Zurich', 'Liege', 'Debrecen',
        'Kazan', 'Urziceni', 'Alkmaar', 'Nicosia', 'Enschede', 'Bursa', 'Zilina', 'Braga', 'London', 'Tel Aviv', 'Plzen',
        'Manchester', 'Zagreb', 'Naples', 'Trabzon', 'Galati', 'Montpellier', 'Malaga', 'Farum', 'Vienna', 'Maribor',
        'Bilbao', 'Malmo', 'Razgrad', 'Ghent', 'Astana', 'Monchengladbach'
    ],
}


# Convert to DataFrame
stadium_df = pd.DataFrame(stadium_data)

# Save DataFrame to Excel
stadium_df.to_excel("stadium_data.xlsx", index=False)


