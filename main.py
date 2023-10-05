import requests
import key
import tweepy
from requests_oauthlib import OAuth1Session

#testing_without_authhandler BRANCH

#consumer key stand for API_key
client = tweepy.Client(
    key.BEARER_TOKEN,
    key.API_KEY,
    key.API_KEY_SECRET,
    key.ACCESS_TOKEN,
    key.ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(key.API_KEY, key.API_KEY_SECRET, key.ACCESS_TOKEN, key.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweet_id_test = 1709758382083817636

#tweet text
# client.create_tweet(text="Hi")

