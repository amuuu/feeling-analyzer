from DataCollector.ElasticHandler import elastic_tweets
from DataCollector.Preprocessor import clean


def write_batch(tweet_dict):
    cleaned_statuses_list = clean.clean(tweet_dict)
    # print("Writing", len(tweet_dict))
    last_batch_index = elastic_tweets.get_last_tweet_id()
    elastic_tweets.write_tweets(cleaned_statuses_list, last_batch_index)
    print("Done writing the batch...")
