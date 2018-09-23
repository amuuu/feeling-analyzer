import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch()


def write_error(error):
    res = es.index(index="errors_index", doc_type='errors_doc', id=get_last_error_index(), body=error)
    print('error logged ', res['result'])


def get_last_error_index():
    return es.count(index='errors_index', doc_type='errors_doc').get('count')
