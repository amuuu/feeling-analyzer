import re
from emoji import UNICODE_EMOJI


def clean(statuses):
    # SAMPLE JSON:
    data = {
        "0": {
            "username": "username",
            "date": "date",
            "content": "content of the tweet.",
            "hashtags": [
                "hashtag1",
                "hashtag2"
            ]
        }
    }

    index = 1
    for s in statuses:
        if s.retweeted_status:
            content = s.retweeted_status.full_text
            user = s.retweeted_status.user.screen_name
        else:
            content = s.full_text
            user = "BestFarsi"

        content_w_line = add_line(content)
        content_wo_links = remove_links(content_w_line)
        content_wo_emoji = remove_emoji(content_wo_links)
        content_cleaned = clean_content(content_wo_emoji)
        # content_wo_hashtags = remove_hashtags(content_wo_emoji)
        content_wo_hashtags = content_cleaned
        hashtags_set = extract_hashtags(content_wo_emoji)

        # print("CONTENT: ", content_wo_hashtags)

        data[str(index)] = {
            "username": user,
            "date": s.created_at,
            "content": content_wo_hashtags,
            "hashtags": hashtags_set
        }
        index += 1

    return data


def extract_username(content):
    username = re.search('RT @(.*): ', content)
    if username is None:
        return "BestFarsi"
    else:
        return username.group(1)


def clean_content(content):
    cleaned_content = re.sub('RT @(.*): ', '', content)
    return cleaned_content


def remove_emoji(content):
    for char in content:
        if char in UNICODE_EMOJI:
            content = content.replace(char, '')
    return content


def remove_links(content):
    content = re.sub(r"http\S+", "", content)
    return content


def extract_hashtags(content):
    hashtags = "\n".join(get_hashtags(content, True)).split('\n')
    return hashtags


def remove_hashtags(content):
    query = content
    stopwords = extract_hashtags(content)
    querywords = query.split()
    resultwords = [word for word in querywords if word.lower() not in stopwords]
    wo_hashtags = ' '.join(resultwords)

    return wo_hashtags


def get_hashtags(text, order=False):
    tags = set([item.strip("#.,-\"\'&*^!") for item in text.split() if (item.startswith("#") and len(item) < 256)])
    return sorted(tags) if order else tags


def add_line(content):
    return content
