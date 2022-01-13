import requests
import sys
from bs4 import BeautifulSoup


def get_text(url: str = None):
    page = requests.get(url, headers=HEADERS, timeout=5)
    if page.status_code == 200:
        return BeautifulSoup(page.text, "lxml")
    else:
        sys.stdout.write(str(page.status_code))
        exit()


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
}
URL = 'https://www.python.org'

soup = get_text(URL)
events = []

for event in soup.findAll(class_='medium-widget event-widget last'):
    for li in event.findAll('li'):
        a = li.find('a')
        date = li.find('time')['datetime'][:10]
        name = a.get_text(strip=True)
        second_url = URL + a['href']
        new_soup = get_text(second_url)
        event_link = new_soup.find('div', class_="event-description").find('a')['href']
        events.append({'link': event_link, 'name': name, 'date': date})


for event in events:
    sys.stdout.write(event['date'] + '\t' +
                     event['name'] + '\n' +
                     event['link'] + '\n' + '\n')
