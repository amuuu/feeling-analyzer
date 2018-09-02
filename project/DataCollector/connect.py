import twitter


class Connector:
    CONSUMER_KEY = "xYxRAO8UgEiykpKhLv3VYs7WP"
    CONSUMER_SECRET = "zQGFiAk18ICLfWGOFRDF2dSVQi9p3r8e3pxil40RQ9RaeiVZtG"
    ACCESS_KEY = "951414619645628416-VrEiqUB4XV0TPneaw5TvPKl3d4fbQtg"
    ACCESS_SECRET = "PZbOIJ9ewRIC8CX43wl7MRfNc81bBofB9RQE7DW0Dcxol"

    def create_client(self):
        api = twitter.Api(consumer_key=self.CONSUMER_KEY,
                          consumer_secret=self.CONSUMER_SECRET,
                          access_token_key=self.ACCESS_KEY,
                          access_token_secret=self.ACCESS_SECRET)
        return api