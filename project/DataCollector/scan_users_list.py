import datetime

from DataCollector import connect


class ScanUsers:
    api = connect.Connector().create_client()

    def scan(self):
        if can_scan_users():
            # get the list of users
            users = self.api.GetFriends(screen_name="BestFarsi")
            # write to the userslist.txt file
            file_name = get_last_updated_list_file_name()
            f = open("../Data/users/%s" % file_name, "w")
            print("Scanning users...")
            print("(writing the file %s)" % file_name)
            for user in users:
                f.write(user.screen_name + "\n")
                # print(user.screen_name)
        else:
            pass


def can_scan_users():
    current_time = get_current_time()
    return update_users_scan_time(current_time)


def update_users_scan_time(current_time):
    last_time_cleaned = read_user_list_last_update_log().split('-')
    current_time_cleaned = current_time.split('-')
    # year
    if int(last_time_cleaned[2]) == int(current_time_cleaned[2]):
        # month
        if int(last_time_cleaned[0]) == int(current_time_cleaned[0]):
            # day
            if int(last_time_cleaned[1]) < int(current_time_cleaned[1]):
                # I'm not sure whether i should compare equals or compare if one is bigger than the other.
                update_user_list_update_log(current_time)
                print("Can update.")
                return True
        else:
            update_user_list_update_log(current_time)
            print("Can update.")
            return True
    else:
        update_user_list_update_log(current_time)
        print("Can update.")
        return True
    return False


def update_user_list_update_log(current_time):
    f = open("../Data/users/list_update_log.txt", "a")
    f.write(current_time + "\n")


def read_user_list_last_update_log():
    f = open('../Data/users/list_update_log.txt')
    lines = f.read().splitlines()
    return lines[-1]


def get_last_updated_list_file_name():
    last_update_date = read_user_list_last_update_log()
    file_name = "userslist-" + last_update_date + ".txt"
    return file_name


def get_current_time():
    return datetime.datetime.now().strftime('%m-%d-%Y')
