import math

from DataCollector.Gatherer import connect, error_handler
from DataCollector.ElasticHandler import elastic_users, batch_writer, elastic_tweets, batch_settings


class TweetGatherer:
    api = connect.Connector().create_client()
    batch_options = batch_settings.BatchSettings()

    def __init__(self):
        self.batch_options.read_settings_file()
        print("Batch size =", self.batch_options.batch_size)

    def gather(self, username, count):
        try:
            statuses = self.api.GetUserTimeline(screen_name=username, count=count)
            return statuses
        except Exception:
            print("ERROR RECEIVING TWEETS FROM @%s" % username)
            error_handler.report_error(username, 1)
            return "ERROR"

    def gather_all(self):
        username_list = elastic_users.get_all_users()
        all_statuses = []
        last_batch = []
        user_count = 1
        for user in username_list:
            username = user.get('_source').get(str(user.get('_id')))
            print("Gathering: @%s" % user.get('_source').get(str(user_count - 1)), " with ID %s." % str(user_count - 1))
            try:
                user_statuses = self.gather(username, 100)
                if user_statuses != 'ERROR':
                    all_statuses.extend(user_statuses)
            except TypeError:
                print("ERROR ON ADDING THIS USER'S TWEETS TO WHOLE LIST: @%s" % user)
                all_statuses.extend({"error": "didn't receive completely"})

            # I'M NOT QUITE SURE ABOUT THE SECOND CONDITION OF IF YET.
            if user_count % self.batch_options.batch_size == 0:
                batch_writer.write_batch(all_statuses)
                all_statuses = []
            elif user_count > math.floor(
                    len(username_list) / self.batch_options.batch_size) * self.batch_options.batch_size:
                last_batch.extend(all_statuses)
            user_count += 1

        if len(last_batch) != 0:
            batch_writer.write_batch(last_batch)

        print("Collecting Job DONE!")
        return True
