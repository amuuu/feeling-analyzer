from DataCollector.Gatherer import connect


class UserDataGatherer:
    api = connect.Connector().create_client()

    def gather(self, username, count):
        # try:
        #     statuses = self.api.GetUserTimeline(screen_name=username, count=count)
        #     return statuses
        # except Exception:
        #     print("ERROR RECEIVING TWEETS FROM @%s" % username)
        #     print("DESCRIPTION:", Exception)
        #     self.er_handler.add_to_log(username, 1)
        pass

    def gather_all(self):
        # username_list = read_users_from_file()
        # all_statuses = []
        # for user in username_list:
        #     print("Gathering: @%s" % user)
        #     try:
        #         all_statuses.extend(self.gather(user, 100))
        #     except TypeError:
        #         print("ERROR ON ADDING THIS USER'S TWEETS TO WHOLE LIST: @%s" % user)
        # self.er_handler.write_log_file()
        # return all_statuses
        pass