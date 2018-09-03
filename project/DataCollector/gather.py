from DataCollector import connect
import json


class Gatherer:
    api = connect.Connector().create_client()

    def gather(self):
        statuses = self.api.GetUserTimeline(screen_name="BestFarsi", count=1000)
        return statuses
