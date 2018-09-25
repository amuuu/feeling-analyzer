from elasticsearch import Elasticsearch

es = Elasticsearch()


def write_tweets(tweets, start_index):
    index=0
    for tweet in tweets:
        res = es.index(index="tweets_index", doc_type='tweets_doc', id=start_index, body=tweets.get(str(index)))
        index += 1
        print(res['result'])


def get_tweets(index):
    # for tweet in es.
    # tweet = es.get(index="tweets_index", doc_type='tweets_doc', id=1)
    pass


def get_last_tweet_date():
    last_index = get_last_tweet_id()
    return es.get(index='tweets_index', doc_type='tweets_doc', id=last_index - 1).get("timestamp")


def get_last_tweet_id():
    print("COUNT: ", es.count(index='tweets_index', doc_type='tweets_doc'))
    return es.count(index='tweets_index', doc_type='tweets_doc').get('count')
