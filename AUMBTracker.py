from WebScraper import *
from FirebaseUtil import *
from TwitterController import sendTweet

checkForLoss()
sendTweet(
    f"It has been {getDaysSinceLoss()} days since AU MBB lost.")
