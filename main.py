import requests
import key
import tweepy
from requests_oauthlib import OAuth1Session

client = tweepy.Client(key.BEARER_TOKEN, key.API_KEY, key.API_KEY_SECRET, key.ACCESS_TOKEN, key.ACCESS_TOKEN_SECRET)
oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=key.API_KEY,
    redirect_uri="",
    scope="",
    client_secret=key.CLIENT_SECRET
)

id = 27851463

auth = tweepy.OAuth1UserHandler(key.API_KEY, key.API_KEY_SECRET, key.ACCESS_TOKEN, key.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
print(oauth2_user_handler.get_authorization_url())

oauth = OAuth1Session(key.API_KEY, client_secret=key.API_KEY_SECRET)

request_token_url = "https://api.twitter.com/oauth/request_token"
response = oauth.fetch_request_token(request_token_url)

resource_owner_key = response.get("oauth_token")
resource_owner_secret = response.get("oauth_token_secret")
print("OAuth Token" % resource_owner_key)


#tweet text
# client.create_tweet(text="Hi")

