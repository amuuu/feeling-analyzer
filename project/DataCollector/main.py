from DataCollector import gather, scan_users_list, clean, save

# This line of code isn't always executed:
# scanner = scan_users_list.ScanUsers().scan()

# statuses_list = gather.Gatherer().gather()
all_statuses = gather.Gatherer().gather_all()
cleaned_statuses_list = clean.clean(all_statuses)
save.write_json(cleaned_statuses_list)

