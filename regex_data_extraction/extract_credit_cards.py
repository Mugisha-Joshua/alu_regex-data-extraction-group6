import re

def extract_credit_cards(text):
    # Regular expression pattern for matching credit card numbers
    credit_card_regex = r'\b(?:\d{4}[ -]?){3}\d{4}\b'

    # Find all matches of the pattern in the text
    return re.findall(credit_card_regex, text)
