import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch()


def write_tweets(tweets):
    index = 0
    for tweet in tweets:
        res = es.index(index="tweets_index", doc_type='tweets_doc', id=index, body=tweets.get(str(index)))
        index += 1
        print("Added %s" % res['result'])


def write_users(users):
    pass