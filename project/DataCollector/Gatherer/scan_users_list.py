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
            for user in users:
                elastic_users.write_users({
                    str(index): user.screen_name,
                    "timestamp": datetime.datetime.now()
                }, index)
                index += 1


def can_scan_users():
    elastic_users.get_last_update_date()
    return True


def calculate_current_time():
    return datetime.datetime.now().strftime('%H-%M-%S--%m-%d-%Y--%A')