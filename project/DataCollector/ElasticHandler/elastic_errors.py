import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch()


def init_error_index():
    return es.index(index="errors_index", doc_type='errors_doc', id=0, body={})


def write_error(error):
    print("LAST  INDEX OF ERROR:", get_last_error_index())
    res = es.index(index="errors_index", doc_type='errors_doc', id=get_last_error_index(), body=error)
    print('error logged ', res['result'])


def get_last_error_index():
    return int(es.count(index='errors_index', doc_type='errors_doc').get('count'))


init_error_index()
