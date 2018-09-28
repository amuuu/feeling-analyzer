from DataCollector.Gatherer import gather_tweets, scan_users_list

print("Scanning users...")
scan_users_list.ScanUsers().scan()

print("Gathering tweets...")
gather_tweets.TweetGatherer().gather_all()

# BUG: IT RECEIVES LAST 50 TWEETS. IT DOESN'T CHECK WHETHER IT'S GETTING DUPLICATE TWEETS.


