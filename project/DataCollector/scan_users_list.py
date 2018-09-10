import datetime

from DataCollector import connect


class ScanUsers:
    api = connect.Connector().create_client()
    last_time = '9-8-2018'

    def scan(self):
        if self.can_scan_users():
            # get the list of users
            users = self.api.GetFriends(screen_name="BestFarsi")
            # write to the userslist.txt file
            date = datetime.datetime.now().strftime('%m-%d-%Y')
            f = open("../Data/users/userslist-%s.txt" % date, "w")
            for user in users:
                f.write(user.screen_name + "\n")
                # print(user.screen_name)
        else:
            pass

    def can_scan_users(self):
        current_time = datetime.datetime.now().strftime('%m-%d-%Y')
        return self.update_users_scan_time(current_time)

    def update_users_scan_time(self, current_time):
        last_time_cleaned = self.last_time.split('-')
        current_time_cleaned = current_time.split('-')
        # year
        if last_time_cleaned[2] == current_time_cleaned[2]:
            # month
            if last_time_cleaned[0] == current_time_cleaned[0]:
                # day
                if int(last_time_cleaned[1]) < int(current_time_cleaned[1]):
                    # I'm not sure whether i should compare equals or compare if one is bigger than the other.
                    self.last_time = current_time
                    print("Can update.")
                    return True
            else:
                self.last_time = current_time
                print("Can update.")
                return True
        else:
            self.last_time = current_time
            print("Can update.")
            return True
        return False
