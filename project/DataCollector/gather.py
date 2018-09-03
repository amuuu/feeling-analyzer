from DataCollector import connect
import json


class Gatherer:
    api = connect.Connector().create_client()

    def gather(self):
        statuses = self.api.GetUserTimeline(screen_name="BestFarsi", count=1000)

        for item in statuses:
            if item.retweeted_status:
                print(item.retweeted_status.full_text)
            else:
                print(item.full_text)
            print("###########################")
        return statuses
