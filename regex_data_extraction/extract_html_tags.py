import re

def extract_html_tags(text):
    html_regex = r'<[^>]+>'
    return re.findall(html_regex, text)
