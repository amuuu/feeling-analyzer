from DataCollector import connect


class Gatherer:
    api = connect.Connector().create_client()

    def gather(self, username, count):
        statuses = self.api.GetUserTimeline(screen_name=username, count=count)
        return statuses

    def gather_all(self):
        username_list = self.read_users_from_file()
        all_statuses = []
        for user in username_list:
            print("Gathering: @%s" % user)
            all_statuses.extend(self.gather(user, 100))
        return all_statuses

    def read_users_from_file(self):
        f = open('static_files/userslisttest.txt')
        line = f.readline()
        username_list = []
        while line:
            username_list.append(line.replace('\n', ''))
            line = f.readline()
        f.close()
        return username_list
