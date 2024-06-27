import pandas as pd
import json
import requests
import sqlalchemy as db

list_of_matches = []


def getMatches(stage, teamA, teamB):
    global list_of_matches
    url_match_info = "https://euro-20242.p.rapidapi.com/matches"

    header = {
        "x-rapidapi-key": "198410ca98mshf04347dff7b21fcp15903fjsne07b9fe16cc6",
        "x-rapidapi-host": "euro-20242.p.rapidapi.com"
    }

    output = requests.get(url_match_info, headers=header)
    all_teams = output.json()

    winner = None
    # each match will get its own dictionary of data
    match_facts = {}
    for item in all_teams:
        if item['isFinished'] == True:
            if item['stage'] == stage:
                if item['teamA']['team']['name'] == teamA:
                    if item['teamB']['team']['name'] == teamB:
                        winner = item['winningTeam']
                        match_facts['stage'] = stage
                        match_facts['team_a'] = teamA
                        match_facts['team_b'] = teamB
                        team_a_score = item['teamA']['score']
                        match_facts['team_a_score'] = team_a_score
                        team_b_score = item['teamB']['score']
                        match_facts['team_b_score'] = team_b_score
                        match_facts['winning team'] = winner
                        break

    #  error handling: incorrect syntax of inputted information
    if not match_facts:
        print("Incorrect input, please check specifics of match information entered.")
        print(f"No existing match for input: {stage}, {teamA}, {teamB}.")
        return

    url_rank = "https://footapi7.p.rapidapi.com/api/rankings/uefa/countries"

    headers = {
        "x-rapidapi-key": "198410ca98mshf04347dff7b21fcp15903fjsne07b9fe16cc6",
        "x-rapidapi-host": "footapi7.p.rapidapi.com"
    }

    response = requests.get(url_rank, headers=headers)
    all_rankings = response.json()

    # FootAPI capitalizes first letter, so editing country name
    teamA_upper = teamA[0].upper() + teamA[1:]
    teamB_upper = teamB[0].upper() + teamB[1:]

    points_teamA = None
    points_teamB = None

    # iterate through the rankings to find the points for teamA and teamB
    for all_countries in all_rankings['rankings']:
        if all_countries['rowName'] == teamA_upper:
            points_teamA = all_countries["points"]
        elif all_countries['rowName'] == teamB_upper:
            points_teamB = all_countries["points"]

    exp_team_name = None

    # figuring out expected game winner based on points ranking
    if points_teamA > points_teamB:
        exp_team_name = teamA
    elif points_teamB > points_teamA:
        exp_team_name = teamB
    else:
        exp_team_name = "Draw"

    more_points = max(points_teamA, points_teamB)
    less_points = min(points_teamA, points_teamB)

    # ratio of goals for expected winning team
    exp = int(more_points//less_points)

    if exp_team_name == "Draw":
        match_facts['expectation'] = 'Draw'
    else:
        match_facts['expectation'] = f'+{exp} {exp_team_name}'
    if match_facts not in list_of_matches:
        list_of_matches.append(match_facts)

    return list_of_matches


#getMatches('groupStage', 'belgium', 'slovakia')
#getMatches('groupStage', 'scotland', 'germany')
getMatches('groupStage', 'germany', 'scotland')
#getMatches('groupStage', 'narnia', 'scotland')
#getMatches('groupstage', 'germany', 'scotland')
#getMatches('roundOfSixteen', 'switzerland', 'italy')

# handling creating the SQL table

if not list_of_matches:
    print("Unable to create table.")
else:
    dataf = pd.DataFrame(list_of_matches)
    engine = db.create_engine('sqlite:///euros2024.db')
    dataf.to_sql('all_matches', con=engine, if_exists='replace', index=False)
    with engine.connect() as connection:
        query_result = (
            connection.execute(db.text("SELECT * FROM all_matches;"))
            .fetchall()
        )
        print(pd.DataFrame(query_result))
