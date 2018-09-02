import oauth2
import oauth2 as oauth
import os
import json

CONSUMER_KEY = "xYxRAO8UgEiykpKhLv3VYs7WP"
CONSUMER_SECRET = "zQGFiAk18ICLfWGOFRDF2dSVQi9p3r8e3pxil40RQ9RaeiVZtG"
ACCESS_KEY = "951414619645628416-VrEiqUB4XV0TPneaw5TvPKl3d4fbQtg"
ACCESS_SECRET = "PZbOIJ9ewRIC8CX43wl7MRfNc81bBofB9RQE7DW0Dcxol"

# consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
# access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
# client = oauth.Client(consumer, access_token)

# URL = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=BestFarsi"


# URL = "https://api.twitter.com/1.1/statuses/home_timeline.json"
# print("Connecting...")
#
# response, data = client.request(URL)
# tweets = json.loads(data)
# for tweet in tweets:
#     print(tweet['text'])

# def oauth_req(url, key, secret, http_headers=None, post_body=b"", http_method="GET"):
#     consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
#     token = oauth2.Token(key=key, secret=secret)
#     client = oauth2.Client(consumer, token)
#     resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers, )
#     return content
#
#
# home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/home_timeline.json', ACCESS_KEY, ACCESS_SECRET)
#
# data = home_timeline.json()
#
# print(data)


import twitter

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_KEY,
                  access_token_secret=ACCESS_SECRET)
statuses = api.GetUserTimeline(screen_name="BestFarsi", count=1000)
for s in statuses:
    print(s.created_at)
    print(s.text)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
