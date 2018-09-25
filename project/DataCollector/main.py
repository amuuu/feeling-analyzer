from DataCollector.Gatherer import gather_tweets, scan_users_list

scan_users_list.ScanUsers().scan()

# gather_tweets.TweetGatherer().gather_all()

# BUG: IT RECEIVES LAST 50 TWEETS. IT DOESN'T CHECK WHETHER IT'S GETTING DUPLICATE TWEETS.


