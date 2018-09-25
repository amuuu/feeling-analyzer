import datetime

from DataCollector.Gatherer import connect
from DataCollector.ElasticHandler import elastic_users


class ScanUsers:
    api = connect.Connector().create_client()

    def scan(self):
        if can_scan_users():
            # get the list of users
            users = self.api.GetFriends(screen_name="BestFarsi")
            print("Getting users from API...")
            index = 0
            for user in users:
                print("User %s was added to users list." % user.screen_name)
                elastic_users.write_user({
                    str(index): user.screen_name,
                    "timestamp": datetime.datetime.now()
                }, index)
                index += 1


def can_scan_users():
    last_update_day = get_day(elastic_users.get_last_update_date())
    rnow_day = now_day()
    if last_update_day == rnow_day:
        print("# ERROR: Can't update users checking list")
        return False
    else:
        print("# Can update users checking list!")
        return True


def get_day(time):
    day = time[8] + time[9]
    return int(day)


def now_day():
    return int(datetime.datetime.now().day)
