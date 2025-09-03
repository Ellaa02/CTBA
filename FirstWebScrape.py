import requests
from bs4 import BeautifulSoup

# URL of the event page
url = "https://www.python.org/events"
req = requests.get(url) # request library allows you to interact with URLs

# Parse the HTML content
soup = BeautifulSoup(req.text, 'lxml')

# Find the event list
events = soup.find('ul', {'class':'list-recent-events'}).find_all('li')

# Loop through and print event details
for event in events:
    title = event.find('h3').get_text(strip=True)
    location = event.find('span', 
                          {'class': 'event-location'}).get_text(strip=True)
    date = event.find('time').get_text(strip=True)
    
    print(f"Title: {title}")
    print(f"Location: {location}")
    print(f"Date: {date}")
    print("-" * 40)