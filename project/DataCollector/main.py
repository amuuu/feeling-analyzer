from DataCollector import gather, scan_users_list, clean, save

# This line of code isn't always executed:
# scanner = scan_users_list.ScanUsers().scan()

statuses_list = gather.Gatherer().gather()
cleaned_statuses_list = clean.clean(statuses_list)
save.write_json(cleaned_statuses_list)
