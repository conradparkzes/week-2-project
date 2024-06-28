# Euro 2024 

## What is the Euro?
- The Euro is a football competition hosted by the Union of
European Football Association. 24 teams representing the top
European nations are currently competing to prove which country
is the best.

## Overview of our files
- The euros.py file contains all of the logic for taking in input from
the user, querying the APIs, and creating a table with their request
The test_euro.py file tests the output from the getMatches() function,
ensuring that the user receives the correct output based on their input.

## How to use our project
- Go to the [Euro 2024 API](https://rapidapi.com/yuvr99-WHTEITBQbOc/api/euro-20242)
and the [FootApi](https://rapidapi.com/fluis.lacasse/api/footapi7), sign up for the
Rapid API site, and subscribe to the APIs with the free plan. You use the
same Rapid API key to use all APIs on the site, so navigate to one of the 
endpoints, click on the Code Snippets tab on the right, choose Python as
the Target from the drop-down menu. Copy the value after
'x-rapidapi-key': and paste it in lines 35 and 71 in euros.py, indicated in
the comments.
- Clone our repository and cd into week-2-project
- No need to download any libraries, we provide everything
- We use the function:
    ```
    getMatches()
    ```
    that will prompt 'stage', 'teamA', and 'teamB' from you in the terminal,
    where stage is the type of stage, teamA is the first country, and
    teamB is the second country
    - You must use one of the 5 stage names provided in the mixedCase
format, any other form will not work (groupStage, roundOfSixteen,
semiFinal, quarterFinal, final)
    - Team names must be all lowercase, with a space if necessary
(england, netherlands, france, switzerland, etc)
    - Team names must be in order of how they are displayed on the
brackets. ex: on day 1, germany and scotland competed. Entering
stage = groupStage, teamA = scotland, teamB = germany will NOT work because
every bracket displays germany vs. scotland. Refer to this [site](https://www.espn.com/soccer/schedule/_/date/20240614/league/uefa.euro)
for the correct order.
    - The game must be completed, any future game that has not yet occurred
is invalid input. Incorrect input will warrant an error statement in the terminal
- You can make as many searches as you would like (until your API rate
limit is reached). When ready, open the terminal, make sure you're in
week-2-project, and run:
    ```
    python3 euros.py
    ```
    which will print a neatly organized table to your terminal with the competitors,
    the winner, the score, and the expected result based on this [site](https://www.uefa.com/nationalassociations/uefarankings/country/?year=2024)
    that ranks every European nation on a points system
