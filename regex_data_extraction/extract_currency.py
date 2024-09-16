import re

def extract_currency(text):
    currency_regex = r'\$\s?\d+(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_regex, text)
