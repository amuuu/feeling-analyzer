import datetime
import sys

from elasticsearch import Elasticsearch

es = Elasticsearch()


def clean_indice(index, doc_type):
    # es.delete(index=index, doc_type=doc_type)
    es.delete_by_query(index=index, doc_type=doc_type, body={"query": {"match_all": {}}})


def clean_tweets():
    clean_indice('tweets_index', 'tweets_doc')
    # print('Tweets index cleaned successfully.')


def clean_users():
    clean_indice('users_index', 'users_doc')
    # print('Users index cleaned successfully.')


def create_index(name):
    es.indices.create(index=name, ignore=400)
    print('Index %s created successfully.' % name)


def run_from_terminal(args):
    if args[1] == "create_index":
        create_index(args[2])
        print("Created index %s successfully." % args[2])
    elif args[1] == "clean_indice":
        clean_indice(args[2].split('index=', ''),
                     args[3].split('doc_type', ''))
        print("Indice %s cleaned successfully." % args[2])
    elif args[1] == "clean_tweets":
        clean_tweets()
        print("Tweets index cleaned successfully.")
    elif args[1] == "clean_users":
        clean_users()
        print("Users index cleaned successfully.")
    else:
        print("INVALID COMMAND.")


run_from_terminal(sys.argv)
