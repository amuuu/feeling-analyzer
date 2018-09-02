import re
from emoji import UNICODE_EMOJI


def clean(statuses):
    data = {
        "0": {
            "username": "username",
            "date": "date",
            "content": "content of the tweet.",
            # "hashtags": {
            #     "hashtag1",
            #     "hashtag2"
            # }
        }
    }

    index = 1
    for s in statuses:
        content_wo_links = remove_links(s.text)
        content_wo_emoji = remove_emoji(content_wo_links)
        username = extract_username(content_wo_emoji)
        content_wo_emoji = clean_content(content_wo_emoji)
        # content_wo_hashtags = remove_hashtags(content_wo_emoji)
        content_wo_hashtags = content_wo_emoji
        # hashtags_set = extract_hashtags(content_wo_emoji)

        data[str(index)] = {
            "username": username,
            "date": s.created_at,
            "content": content_wo_hashtags,
            # "hashtags": hashtags_set
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
    print(content)
    cleaned_content = re.sub('RT @(.*): ', '', content)
    # print("CONTENT: ", cleaned_content)
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
    hashtags = "\n".join(get_hashtags(content, True))
    return hashtags


# def remove_hashtags(content):
#     hashtags = "\n".join(get_hashtags(content, True))
#     content_list = content.split(" ", ".", "،", ".", ",")
#     for word in content_list:
#         if word in hashtags:
#             content_list.replace(word, '')
#     return hashtags


def get_hashtags(text, order=False):
    tags = set([item.strip("#.,-\"\'&*^!") for item in text.split() if (item.startswith("#") and len(item) < 256)])
    return sorted(tags) if order else tags
