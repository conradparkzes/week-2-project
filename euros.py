import pandas as pd
import json
import requests
import sqlalchemy as db

list_of_matches = []

def getMatches(stage, teamA, teamB):
    #  params = stage, teamA, teamB
    url = "https://euro-20242.p.rapidapi.com/matches"

    headers = {
	"x-rapidapi-key": "462634edaamshbb062caa9f855bfp1d5ea4jsna71d5565c6f4",
	"x-rapidapi-host": "euro-20242.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    all_teams = response.json()

    #print(json.dumps(all_teams, indent=4))


    



    winner = None
    for item in all_teams:
        match_facts = {}
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
                   list_of_matches.append(match_facts)


    return list_of_matches
    #print(winner)
    






# curl -X 'GET' -H 'accept: application/json' -H 'X-API-Key: 
#eyJhbGciOiJSUzI1NiIsImtpZCI6Img4LThRX1YwZnlUVHRPY2ZXUWFBNnV2bktjcnIyN1YzcURzQ2Z4bE44MGMiLCJ0eXAiOiJKV1QifQ.eyJhY2Nlc3NfdGllciI6ImFmZmlsaWF0ZSIsImV4cCI6MjAzNDYyMzg4MSwiaWF0IjoxNzE5MjYzODgxLCJqdGkiOiIzYzJlZDYwZi05Mzc2LTRkY2YtOTgwZi0wNzFkZjE2N2ZmNmYiLCJzdWIiOiI3Nzg0OGQ1My03NmNiLTQ1NzMtYjlkZC1hMWY2YjM5NDUxYjQiLCJ0ZW5hbnQiOiJjbG91ZGJldCIsInV1aWQiOiI3Nzg0OGQ1My03NmNiLTQ1NzMtYjlkZC1hMWY2YjM5NDUxYjQifQ.jDm9M1fI6dwQiLFIuJQi0GfI9Fz6EKJfghElky1c8BUT65FBlIBB4QiHZ17SxqePiwXw9pwJU_LBM4Buhu3rEXPAaLznRLaewP4ezRHZsSrzyCAwFolvkKNXuM4GcaJAFjPJXdBrFJeYc8pNtN-503FuwxTuivf5i_zm9vYFYVtMJwOlRcnjJsN6GP4OMho7DmZfFrmGenZBoKh8cIHV-QYvksZOtnx_X8ygmYabxKlHchoN0MgQV7qQpPDkodlc9V1KnYspA-isC7qn9eQS_phRFV1GVLzjSAGWjnrQpo6lmEObD_JWOU260goi9Anq-jjGAzVLeqk5Wa1hlaFrxg' \
#'https://sports-api.cloudbet.com/pub/v2/odds/competitions/soccer-international-euro-cup'

getMatches('groupStage', 'belgium', 'slovakia')
getMatches('groupStage', 'germany', 'scotland')
print(list_of_matches)
dataf = pd.DataFrame(list_of_matches)
    
engine = db.create_engine('sqlite:///euros2024.db')
dataf.to_sql('all_matches', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM all_matches;")).fetchall()
    print(pd.DataFrame(query_result))
