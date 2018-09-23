import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch()


def write_users(user, index):
    res = es.index(index="users_index", doc_type='users_doc', id=index, body=user)
    print("user %s" % user, res['result'])


def get_users():
    pass


def get_last_update_date():
    last_index = get_last_update_index()
    return es.get(index='users_index', doc_type='users_doc', id=last_index - 1).get('timestamp')


def get_last_update_index():
    return es.count(index='users_index', doc_type='users_doc').get('count')

