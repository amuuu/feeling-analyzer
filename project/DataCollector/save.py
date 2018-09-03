import io
import json
import datetime


def write_json(data):
    file_name = calculate_current_time()
    with io.open('../Data/%s.json' % file_name, 'a', encoding='utf8') as outfile:
        str_ = json.dumps(data,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(str_)
    print("Done.")


def calculate_current_time():
    current = datetime.datetime.now().strftime('%H-%M-%S--%m-%d-%Y--%A')
    return current
