import re

def extract_time(text):
    time_24_regex = r'\b(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])\b'
    time_12_regex = r'\b([1-9]|1[0-2]):([0-5][0-9])\s*(AM|PM)\b'
    
    times_24 = re.findall(time_24_regex, text)
    times_12 = re.findall(time_12_regex, text)
    
    return times_24, times_12
