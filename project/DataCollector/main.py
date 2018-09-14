from DataCollector import gather, scan_users_list, clean, save, tir_calculator

# Scan @BestFarsi's following
# scanner = scan_users_list.ScanUsers().scan()


# Get last tweets from the users list
# all_statuses = gather.Gatherer().gather_all()
# cleaned_statuses_list = clean.clean(all_statuses)
# save.write_json(cleaned_statuses_list)
# BUG: IT RECEIVES LAST 50 TWEETS. IT DOESN'T CHECK WHETHER IT'S GETTING DUPLICATE TWEETS.

tir_calculator.read_fame_json()