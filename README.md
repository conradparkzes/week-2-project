# Euros 2024 

## What is the Euros?
- The Euros is a football competition hosted by the Union of
European Football Asssociation. 24 teams representing different
European nations are currently competing to prove which country
is the best.

## How to use our project
- Clone our repository and cd into week-2-project
- No need to download any libraries, we provide everything
- make calls to:
    ```
    getMatches (stage, teamA, teamB)
    ```
    where stage is the type of stage and teamA is the first country and
    teamB is the second country
    - you must use one of the 4 stage names provided in the mixedCase
format, any other form will not work (groupStage, roundOfSixteen,
semiFinal, quarterFinal, final)
    - team names must be all lowercase, with a space if necessary
(england, czech republic, turkiye, netherlands)
    - team names must be in order of how they are displayed on the
brackets. ex: on day 1, germany and scotland competed. entering
getMatches(groupStage, scotland, germany) will NOT work because every
bracket displays germany vs. scotland. refer to this [site](https://www.espn.com/soccer/schedule/_/date/20240614/league/uefa.euro)
for the correct order 
    - the game must be completed, any future game that has not yet occurred
is invalid input. incorrect input will warrant an error statement in the terminal
- you can make as many calls to getMatches as you would like. when ready,
open the terminal, make sure you're in week-2-project, and run:
    ```
    python3 euros.py
    ```
    which will print a neatly organized table to your terminal with the competitors,
    the winner, the score, and the expected result based on this [site](https://www.uefa.com/nationalassociations/uefarankings/country/?year=2024)
    that ranks every European nation on a points system
