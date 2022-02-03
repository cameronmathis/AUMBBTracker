from Utils.Util import getDaysSinceLoss
from Utils.TwitterUtil import sendTweet

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
