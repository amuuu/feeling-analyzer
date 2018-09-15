import datetime
import json


def erase_duplicate(new_data):
    last_data = read_last_tweet_json()
    cleaned_data = compare_json(last_data, new_data)
    return cleaned_data


def compare_json(last_data, new_data):
    # TOO INEFFICIENT!
    for new_d in last_data:
        for old_d in new_data:
            if old_d == new_d:
                new_data.pop(new_d)
    return new_data


def read_last_tweet_json():
    prev_time_name = get_last_updated_json_name()
    with open('../Data/users/%s' % prev_time_name, 'r') as f:
        timeline_dict = json.load(f)
    return timeline_dict


def get_last_updated_json_name():
    f = open('../Data/timelines_log.txt')
    lines = f.read().splitlines()
    return lines[-1]