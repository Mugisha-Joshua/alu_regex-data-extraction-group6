import re

def extract_phone_numbers(text):
    # Define a regular expression pattern for matching phone numbers
    phone_regex = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    # Find all phone numbers in the text using the regex pattern
    return re.findall(phone_regex, text)
