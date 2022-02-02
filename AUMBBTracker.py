from WebScraper import getCurrentRecord
from FirebaseUtil import *
from TwitterController import sendTweet

'''
Returns a boolean indicating if a game has been played
'''


def checkForGame():
    previousRecord = getPreviousRecord()
    currentRecord = getCurrentRecord()

    if (previousRecord == currentRecord):
        return False

    return True


'''
Returns a boolean indicating if a loss has occurred
'''


def checkForLoss():
    if not (checkForGame()):
        setDaysSinceLoss(getDaysSinceLoss() + 1)
        return

    # get previous losses
    previousRecord = getPreviousRecord()
    splitPreviousRecord = previousRecord.split("-", 1)
    previousLosses = splitPreviousRecord[1]
    # get current losses
    currentRecord = getCurrentRecord()
    splitCurrentRecord = currentRecord.split("-", 1)
    currentLosses = splitCurrentRecord[1]
    # compare losses
    if (previousLosses == currentLosses):
        setDaysSinceLoss(getDaysSinceLoss() + 1)
        return

    setDaysSinceLoss(0)
    return


'''
Main method to run the application
'''


def main():
    checkForLoss()

    sendTweet(
        f"It has been {getDaysSinceLoss()} days since AU MBB lost.")


main()
