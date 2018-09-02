import json

from DataCollector import connect


class ScanUsers:
    api = connect.Connector().create_client()

    def scan(self):
        # get the list of users
        users = self.api.GetFriends(screen_name="BestFarsi")

        # write to the userslist.txt file
        f = open("static_files/userslist.txt", "a")
        for user in users:
            f.write(user.screen_name + "\n")
            print(user.screen_name)
