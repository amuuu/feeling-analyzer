import oauth2 as oauth
import json

CONSUMER_KEY = "LJV92R5PtMCnuoMxngAdByL7v"
CONSUMER_SECRET = "syLRObDZ1Ahuf72AcAOTdmisRKsATdP9dpqzPVZxhSkGYcIczX"
ACCESS_KEY = " 951414619645628416-p4firNklmBlal1ssMn70xc7124cqIlc"
ACCESS_SECRET = "Hxbgw54DJs5Ny2pZnZQ3WvfN3817S6EkUkmdzLuQhM5m6"


consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

URL = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=BestFarsi"
response, data = client.request(URL)

tweets = json.loads(data)
for tweet in tweets:
    print(tweet['text'])
# def oauth_req(url, key, secret, http_headers=None, post_body="", http_method="GET"):
#     consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
#     token = oauth2.Token(key=key, secret=secret)
#     client = oauth2.Client(consumer, token)
#     resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
#     return content
#
#
# home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/home_timeline.json', 'abcdefg', 'hijklmnop')
#
# data = home_timeline.json()
#
# print(data)
