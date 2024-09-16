import re

def extract_urls(text):
    url_regex = r'https?://[^\s/$.?#].[^\s]*[^\s.,;)]'
    return re.findall(url_regex, text)
