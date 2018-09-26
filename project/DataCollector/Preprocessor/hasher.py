import hashlib


def hash_tweet(tweet_content: str) -> str:
    return hashlib.sha512(tweet_content.encode('utf-8')).hexdigest()
