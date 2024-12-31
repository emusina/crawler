import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

urls = [
    "https://website0.com",
    "https://website1.com"
]

def crawl_and_save(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract text from body
    body_text = soup.body.get_text(separator=' ', strip=True)

    # Create a dictionary to hold the data
    data = {
        "url": url,
        "body_text": body_text
    }

    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M")

    # Create a filename dynamically with the timestamp
    filename = os.path.join(r"D:\...\CrawlerData", f"{url.replace('http://', '').replace('https://', '').replace('/', '_')}_parsed_at{timestamp}.json")

    # Ensure the directory exists
    os.makedirs(r"D:\...\CrawlerData", exist_ok=True)

    # Save the data in a JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Data from {url} saved to {filename}")

# Crawl each URL
for url in urls:
    crawl_and_save(url)