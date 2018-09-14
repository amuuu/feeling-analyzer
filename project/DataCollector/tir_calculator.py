import json


class TIRCalculator:
    days_pos_values = [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]
    days_neg_values = [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]

    def calculate_tir(self, status):
        tir = 0.65 * ((7 * status.retweet_count / 1000) + (3 * status.user.favourites_count / 10000)) + 0.35 * (
            get_fame(status.user.screen_name))

        return tir


def get_fame(screen_name):
    return read_fame_json(screen_name)


def read_fame_json(screen_name):
    with open('../Data/users/fame_rate.json', 'r') as f:
        fame_dict = json.load(f)

    fame_rate = 5
    index = 0
    for user in fame_dict:
        if fame_dict.get(str(index)).get("username") == screen_name:
            fame_rate = fame_dict.get(str(index)).get("rate")
        index += 1

    return fame_rate
