import re
import requests
from cryptography.fernet import Fernet

# Function to detect sensitive data in content
def detect_sensitive_data(content):
    patterns = {
        "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        "Phone Number": r"\b\d{10}\b|\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",
        "Address": r"\d{1,5}\s\w+(\s\w+)*,\s\w+,\s\w+",
    }
    results = {}
    for label, pattern in patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            results[label] = matches
    return results

# Function to analyze URLs
def analyze_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"URL '{url}' is accessible.")
        else:
            print(f"URL '{url}' returned status code {response.status_code}.")
    except Exception as e:
        print(f"Error accessing URL '{url}': {e}")

# Privacy Tips
def privacy_suggestions(results):
    suggestions = []
    if "Email" in results or "Phone Number" in results:
        suggestions.append("Avoid sharing personal contact details in public content.")
    if "Address" in results:
        suggestions.append("Do not share your home address publicly.")
    return suggestions

# Simulates a user post
user_post = """
Hey everyone, contact me at john.doe@example.com or 123-456-7890.
Here's my location: 123 Main St, Springfield, IL. 
Also, check out this website: http://example.com/malware
"""

# Project execution
print("Analyzing user content...\n")
sensitive_data = detect_sensitive_data(user_post)
if sensitive_data:
    print("Sensitive Data Found:")
    for label, data in sensitive_data.items():
        print(f" - {label}: {', '.join(data)}")

    suggestions = privacy_suggestions(sensitive_data)
    print("\nPrivacy Suggestions:")
    for suggestion in suggestions:
        print(f" - {suggestion}")
else:
    print("No sensitive data found.")

print("\nAnalyzing URLs...")
analyze_url("http://example.com/malware")
