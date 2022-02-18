from auth import (
    twitterAPIKey,
    twitterAPISecretKey,
    twitterAccessToken,
    twitterAccessTokenSecret
)
import tweepy
from datetime import datetime
import logging
# for file logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='AUMBBTracker.log', force=True, level=logging.INFO)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitterAPIKey, twitterAPISecretKey)
auth.set_access_token(twitterAccessToken, twitterAccessTokenSecret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    logging.info("Twitter authentication successful.")
except Exception as exception:
    logging.error(
        f"An error occurred during Twitter authentication. | Exception \"{exception}\"")
    quit()


# Sends a tweet
# Parameters:
#     txt - a string indicating the tweet to be sent
def sendTweet(txt):
    try:
        api.update_status(status=txt)
        logging.info(f"Tweet sent with the content: \"{txt}\"")
    except Exception as exception:
        logging.error(
            f"An error occurred when sending tweet: \"{txt}\" | Exception: \"{exception}\"")

    return
