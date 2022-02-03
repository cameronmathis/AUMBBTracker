from datetime import datetime
import tweepy
from auth import (
    twitterAPIKey,
    twitterAPISecretKey,
    twitterAccessToken,
    twitterAccessTokenSecret
)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitterAPIKey, twitterAPISecretKey)
auth.set_access_token(twitterAccessToken, twitterAccessTokenSecret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Twitter authentication successful\n")
except:
    print("Error during Twitter authentication\n")

'''
Sends a tweet

Parameters: 
    txt - a string indicating the tweet to be sent
'''


def sendTweet(txt):
    api.update_status(status=txt)
    print(f"\nTweet sent at {datetime.now()}")
    print(f"Tweet: \"{txt}\"\n")

    return
