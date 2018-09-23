import twitter


class Connector:
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_KEY = ""
    ACCESS_SECRET = ""

    def __init__(self):
        self.read_credentials()

    def create_client(self):
        api = twitter.Api(consumer_key=self.CONSUMER_KEY,
                          consumer_secret=self.CONSUMER_SECRET,
                          access_token_key=self.ACCESS_KEY,
                          access_token_secret=self.ACCESS_SECRET,
                          tweet_mode='extended')
        return api

    def read_credentials(self):
        credentials = read_credentials_file()
        self.CONSUMER_KEY = credentials[0]
        self.CONSUMER_SECRET = credentials[1]
        self.ACCESS_KEY = credentials[2]
        self.ACCESS_SECRET = credentials[3]


def read_credentials_file():
    f = open('../DataCollector/Gatherer/credentials.txt')
    line = f.readline()
    credentials = []
    while line:
        credentials.append(line.replace('\n', ''))
        line = f.readline()
    f.close()
    return credentials
