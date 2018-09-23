import datetime
import io
from DataCollector.ElasticHandler import elastic_errors


def report_error(username, status):
    elastic_errors.write_error({
        status: username,
        'time': datetime.datetime.now()
    })


def get_status(status):
    if status == 1:
        return 'RECEIVING-FROM-TWITTER-API'

    return 0
