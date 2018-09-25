from elasticsearch import Elasticsearch
from DataCollector.Gatherer import scan_users_list

es = Elasticsearch()


def write_user(user, index):
    res = es.index(index="users_index", doc_type='users_doc', id=index, body=user)
    print("user %s" % user, res['result'])


def get_user(index):
    return es.get(index='users_index', doc_type='users_doc', id=index)


def get_all_users():
    last_update_day = get_last_update_day()
    users = []
    for i in range(get_last_update_index() - 1, -1, -1):
        if last_update_day == get_user_adding_day(i):
            print("USER %s ADDED." % get_user(i))
            users.append(get_user(i))
    return users


def get_last_update_date():
    last_index = get_last_update_index()
    return es.get(index='users_index', doc_type='users_doc', id=last_index - 1).get('_source').get('timestamp')


def get_user_adding_day(index):
    time = es.get(index='users_index', doc_type='users_doc', id=index).get('_source').get('timestamp')
    return int(time[8] + time[9])


def get_last_update_index():
    return es.count(index='users_index', doc_type='users_doc').get('count')


def get_last_update_day():
    day_ = get_last_update_date()
    update_day = day_[8] + day_[9]
    return int(update_day)
