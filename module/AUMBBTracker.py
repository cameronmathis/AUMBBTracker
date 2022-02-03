from datetime import date, datetime
from utils.TwitterUtil import sendTweet
from utils.ScraperUtil import *
from utils.DatabaseUtil import *

'''
Checks to see if a loss has occurred

Returns a boolean
'''


def haveLost():
    # get previous losses
    previousRecord = getRecord()
    previousLosses = previousRecord.split("-", 1)[1]
    # get current losses
    currentRecord = scrapeCurrentRecord()
    currentLosses = currentRecord.split("-", 1)[1]
    # compare losses
    if not (previousLosses == currentLosses):
        return True

    return False


'''
Calculates the number of days since a loss

Returns a int
'''


def getDaysSinceLoss():
    if (haveLost()):
        setLastLossDate(scrapeLastLossDate())

    today = datetime.strptime(date.today().strftime("%m/%d/%Y"), "%m/%d/%Y")
    lastLostDate = datetime.strptime(getLastLossDate(), "%m/%d/%Y")
    daysSinceLoss = today - lastLostDate

    return daysSinceLoss.days


'''
Main method to run the application
'''


def main():
    print(f"It has been {getDaysSinceLoss()} days since AU MBB lost.")
    # sendTweet(
    #     f"It has been {getDaysSinceLoss()} days since AU MBB lost.")


# call the main method
if __name__ == "__main__":
    main()
