import requests
from bs4 import BeautifulSoup


KEYWORDS = {'дизайн', 'фото', 'web', 'python', "C++*"}
url = 'https://habr.com/ru/all/'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    # print(article)
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = {hub.text.strip() for hub in hubs}
    if KEYWORDS & hubs:
        current_time = article.find('time').attrs.get('title')
        title = article.find('h2')
        href = title.find('a').attrs.get('href')
        print(current_time, title.text, url + href)
