from DataCollector import connect, error_handler, scan_users_list
from DataCollector.scan_users_list import get_last_updated_list_file_name


class Gatherer:
    api = connect.Connector().create_client()
    er_handler = error_handler.ErrorHandler()

    def gather(self, username, count):
        try:
            statuses = self.api.GetUserTimeline(screen_name=username, count=count)
            return statuses
        except Exception:
            print("ERROR RECEIVING TWEETS FROM @%s" % username)
            print("DESCRIPTION:", Exception)
            self.er_handler.add_to_log(username, 1)

    def gather_all(self):
        username_list = read_users_from_file()
        all_statuses = []
        for user in username_list:
            print("Gathering: @%s" % user)
            try:
                all_statuses.extend(self.gather(user, 100))
            except TypeError:
                print("ERROR ON ADDING THIS USER'S TWEETS TO WHOLE LIST: @%s" % user)
        self.er_handler.write_log_file()
        return all_statuses


def read_users_from_file():
    last_update = get_last_updated_list_file_name()
    f = open('../Data/users/%s' % last_update)
    line = f.readline()
    username_list = []
    while line:
        username_list.append(line.replace('\n', ''))
        line = f.readline()
    f.close()
    return username_list
