import requests
import key
import tweepy

client = tweepy.Client(key.BEARER_TOKEN, key.API_KEY, key.API_KEY_SECRET, key.ACCESS_TOKEN, key.ACCESS_TOKEN_SECRET)
oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=key.API_KEY,
    redirect_uri="",
    scope="",
    client_secret=key.CLIENT_SECRET
)
print(oauth2_user_handler.get_authorization_url())

client.create_tweet(text="Hi")


