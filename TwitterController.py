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
    print("\nTwitter authentication successful\n")
except:
    print("\nError during Twitter authentication\n")

'''
Sends a tweet

Parameters: 
    txt - the tweet to be sent
'''
def sendTweet(txt):
    api.update_status(status=txt)
    print("\nTweet sent\n")