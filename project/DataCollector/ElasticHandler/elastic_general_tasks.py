import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch()


def clean_indice(index, doc_type):
    # es.delete(index=index, doc_type=doc_type)
    es.delete_by_query(index=index, doc_type=doc_type, body={"query": {"match_all": {}}})


def clean_tweets():
    clean_indice('tweets_index', 'tweets_doc')
    print('Tweets index cleaned successfully.')


def clean_users():
    clean_indice('users_index', 'users_doc')
    print('Users index cleaned successfully.')


clean_users()