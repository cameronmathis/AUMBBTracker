import sys
import time
from datetime import timedelta
from WebScraper import *
from TwitterController import sendTweet
from TwilioSMSController import sendSMS

# initialize record
updatedRecord = getCurrentRecord()
storedRecord = getCurrentRecord()

# initialize other variables
haveTweetedPreGame = False

# run the loop every minute as to not overload the CPU
while (not time.sleep(60)):
    # check if a game happens today
    if isGameToday() and not haveTweetedPreGame:
        # convert game time to datetime format
        tipOffTime = getGameTime()
        # convert tip off time from EST to CT
        tipOffTime + timedelta(minutes = -60)
        # check if the game starts within 5 minutes
        now = datetime.now()
        if tipOffTime + timedelta(minutes = -5) < now < tipOffTime:
            sendTweet(f"Today's game {getGamesLocation()} {getGamesOpponent()} is about to tip off.")
            haveTweetedPreGame = True

    # get updated record
    updatedRecord = getCurrentRecord()
    # check if record has changed
    if storedRecord != updatedRecord:
        # store new record
        storedRecord = getCurrentRecord()
        sendTweet(f"The result of today's game {getGamesLocation()} {getGamesOpponent()} was a {getGamesResult()}, with a final score of {getGamesScore()}.")
        if len(sys.argv) == 2:
            sendSMS(f"The result of today's game {getGamesLocation()} {getGamesOpponent()} was a {getGamesResult()}, with a final score of {getGamesScore}.", sys.argv[1])
        haveTweetedPreGame = False
