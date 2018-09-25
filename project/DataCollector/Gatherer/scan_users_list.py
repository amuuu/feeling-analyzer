import datetime

from DataCollector.Gatherer import connect
from DataCollector.ElasticHandler import elastic_users


class ScanUsers:
    api = connect.Connector().create_client()

    def scan(self):
        if can_scan_users():
            # get the list of users
            users = self.api.GetFriends(screen_name="BestFarsi")
            index = 0
            print("Getting users from API...")
            for user in users:
                print("User %s was added to users list." % user.screen_name)
                elastic_users.write_user({
                    str(index): user.screen_name,
                    "timestamp": datetime.datetime.now()
                }, index)
                index += 1


def can_scan_users():
    # print(elastic_users.get_last_update_date())
    return True


def calculate_current_time():
    return datetime.datetime.now().strftime('%H-%M-%S--%m-%d-%Y')

# can_scan_users()
