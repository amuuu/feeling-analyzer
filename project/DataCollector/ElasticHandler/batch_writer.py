from DataCollector.Gatherer import gather_tweets
from DataCollector.ElasticHandler import elastic_tweets
from DataCollector.Preprocessor import clean


def write_batch(tweet_dict, batch_last_index):
    cleaned_statuses_list = clean.clean(tweet_dict)
    elastic_tweets.write_tweets(cleaned_statuses_list, batch_last_index)