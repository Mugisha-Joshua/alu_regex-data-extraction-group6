import re

def extract_hashtags(text):
    hashtag_regex = r'#\w+'
    return re.findall(hashtag_regex, text)
