from DataCollector import connect


class Gatherer:
    api = connect.Connector().create_client()

    def gather(self):
        statuses = self.api.GetUserTimeline(screen_name="BestFarsi", count=1000)
        for s in statuses:
            print(s.created_at)
            print(s.text)
