 # You can expand this pattern

import re
import requests

phishing_pattern = r"(.*\.ru|.*\.xyz|.*\.top)" 
#Regex pattern to identify suspicious URLs (example: phishing URLs)
phishing_pattern = r"(.*\.ru|.*\.xyz|.*\.top)"  # You can expand this pattern

def detect_phishing(url):
    if re.search(phishing_pattern, url):
        return f"Suspicious URL detected: {url}"
    return "URL seems safe"

#Example URL to check
url_to_check = "http://example.ru"
print(detect_phishing(url_to_check))


