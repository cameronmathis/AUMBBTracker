import tweepy
from auth import (
    twitterConsumerKey,
    twitterConsumerSecret,
    twitterAccessToken,
    twitterAccessTokenSecret
)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitterConsumerKey, twitterConsumerSecret)
auth.set_access_token(twitterAccessToken, twitterAccessTokenSecret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Twitter authentication successful")
except:
    print("Error during Twitter authentication")

def sendTweet(txt):
    api.update_status(status=txt)
    print("Tweet sent")