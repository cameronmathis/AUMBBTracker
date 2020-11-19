import sys
import time
from datetime import datetime
from sportsreference.ncaab.teams import Teams
from sportsreference.ncaab.schedule import Schedule
from TwitterController import sendTweet
from TwilioSMSController import sendSMS

# look for Auburn in team
for team in Teams():
    if(team.name == "Auburn"):
        auburn = team

# initialize wins/loses
updatedWins = auburn.wins
updatedLosses = auburn.losses 
storedWins = auburn.wins
storedLosses = auburn.losses

# run the loop every minute as to not overload the CPU
while (not time.sleep(60)):
    # get updated wins/losses
    updatedWins = auburn.wins
    updatedLosses = auburn.losses 
    # check if wins or losses have changed
    if(storedWins != updatedWins or storedLosses != updatedLosses):
        # store new wins/losses
        storedWins = auburn.wins
        storedLosses = auburn.losses
        auburnSchedule = Schedule('AUBURN')
        for game in auburnSchedule:
            if(game.datetime.strftime('%Y-%m-%d') == datetime.today().strftime('%Y-%m-%d')):
                sendTweet(f"The result of AUMB's game today against {game.opponent_name} was a {game.result.lower()}, with a final score of {game.points_for}:{game.points_against}.")
                if len(sys.argv) == 2:
                    sendSMS(f"The result of AUMB's game today against {game.opponent_name} was a {game.result.lower()}, with a final score of {game.points_for}:{game.points_against}.", sys.argv[1])
