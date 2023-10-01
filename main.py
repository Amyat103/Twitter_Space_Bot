import requests
import key

headers = {
    "Authorization": f"Bearer {key.BEARER_TOKEN}"
}

r = requests.get("https://api.twitter.com/2/tweets/search/recent?query=from:twitterdev", headers=headers)

print(r.status_code)
print(r.text)
