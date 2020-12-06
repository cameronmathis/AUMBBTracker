import sys
import time
from WebScraper import getCurrentRecord, getGamesOpponent, getGamesResult, getGamesScore
from TwitterController import sendTweet
from TwilioSMSController import sendSMS

# initialize record
updatedRecord = getCurrentRecord()
storedRecord = getCurrentRecord()

# run the loop every minute as to not overload the CPU
while (not time.sleep(60)):
    # get updated record
    updatedRecord = getCurrentRecord()
    # check if record has changed
    if(storedRecord != updatedRecord):
        # store new record
        storedRecord = getCurrentRecord()
        sendTweet(f"The result of today's game against {getGamesOpponent()} get was a {getGamesResult()}, with a final score of {getGamesScore()}.")
        if len(sys.argv) == 2:
            sendSMS(f"The result of today's game against {getGamesOpponent()} was a {getGamesResult()}, with a final score of {getGamesScore}.", sys.argv[1])
