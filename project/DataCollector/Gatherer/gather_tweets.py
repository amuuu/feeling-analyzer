import math

from DataCollector.Gatherer import connect, error_handler
from DataCollector.ElasticHandler import elastic_users, batch_writer, elastic_tweets


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
        last_index = int(elastic_tweets.get_last_tweet_id())
        all_statuses = []
        user_count = 1
        for user in username_list:
            print("Gathering: @%s" % user)
            try:
                all_statuses.extend(self.gather(user, 100))
            except TypeError:
                print("ERROR ON ADDING THIS USER'S TWEETS TO WHOLE LIST: @%s" % user)

            if (user_count % 200 == 0) or user_count > (math.floor(user_count/200)+1):
                batch_writer.write_batch(all_statuses, user_count+last_index)
                all_statuses = []

            user_count += 1
        return "Collecting Job DONE!"
