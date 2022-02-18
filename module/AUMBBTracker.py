from utils.DatabaseUtil import *
from utils.ScraperUtil import *
from utils.TwitterUtil import sendTweet
from datetime import date, datetime
import logging
# for file logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='AUMBBTracker.log', force=True, level=logging.INFO)


# Checks to see if a loss has occurred
# Returns:
#   a boolean
def haveLost():
    # get previous losses
    previousRecord = getRecord()
    previousLosses = previousRecord.split("-", 1)[1]
    # get current losses
    currentRecord = scrapeCurrentRecord()
    currentLosses = currentRecord.split("-", 1)[1]
    # compare losses
    if not (previousLosses == currentLosses):
        # store current record in database
        setRecord(currentRecord)
        return True

    return False


# Calculates the number of days since a loss
# Returns:
#   an int
def getDaysSinceLoss():
    if (haveLost()):
        setLastLossDate(scrapeLastLossDate())

    today = datetime.strptime(date.today().strftime("%m/%d/%Y"), "%m/%d/%Y")
    lastLossDate = datetime.strptime(getLastLossDate(), "%m/%d/%Y")
    daysSinceLoss = today - lastLossDate

    logging.info(
        f"Successfully calculated the days since last loss. | Days: {daysSinceLoss.days}")
    return daysSinceLoss.days


# Main method to run the application
def main():
    daysSinceLoss = getDaysSinceLoss()
    if daysSinceLoss == 1:
        sendTweet(
            f"It has been {daysSinceLoss} day since AU MBB lost.")
    else:
        sendTweet(
            f"It has been {daysSinceLoss} days since AU MBB lost.")


# call the main method
if __name__ == "__main__":
    main()
