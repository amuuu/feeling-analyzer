from DataCollector.ElasticHandler import elastic_tweets
from DataCollector.Preprocessor import clean
from DataCollector.Gatherer import gather_tweets, scan_users_list
from DataCollector.ElasticHandler import elastic_users

# Scan @BestFarsi's following
scanner = scan_users_list.ScanUsers().scan()


# Get last tweets from the users list
# all_statuses = gather_tweets.TweetGatherer().gather_all()
# cleaned_statuses_list = clean.clean(all_statuses)
# save.write_json(cleaned_statuses_list)
# elastic_tweets.write_tweets(cleaned_statuses_list)
# BUG: IT RECEIVES LAST 50 TWEETS. IT DOESN'T CHECK WHETHER IT'S GETTING DUPLICATE TWEETS.


