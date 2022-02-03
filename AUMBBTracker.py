from Utils.Util import getDaysSinceLoss
from Utils.TwitterUtil import sendTweet

'''
Main method to run the application
'''


def main():
    print(f"It has been {getDaysSinceLoss()} days since AU MBB lost.")
    # sendTweet(
    #     f"It has been {getDaysSinceLoss()} days since AU MBB lost.")


main()
