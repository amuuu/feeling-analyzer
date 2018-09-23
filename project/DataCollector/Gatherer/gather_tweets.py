from DataCollector.Gatherer import connect, error_handler
from DataCollector.ElasticHandler import elastic_users, elastic_tweets


class TweetGatherer:
    api = connect.Connector().create_client()

    def gather(self, username, count):
        try:
            statuses = self.api.GetUserTimeline(screen_name=username, count=count)
            return statuses
        except Exception:
            print("ERROR RECEIVING TWEETS FROM @%s" % username)
            error_handler.report_error(username, 1)

    def gather_all(self):
        username_list = elastic_users.get_all_users()
        all_statuses = []
        for user in username_list:
            print("Gathering: @%s" % user)
            try:
                all_statuses.extend(self.gather(user, 100))
            except TypeError:
                print("ERROR ON ADDING THIS USER'S TWEETS TO WHOLE LIST: @%s" % user)
        return all_statuses
