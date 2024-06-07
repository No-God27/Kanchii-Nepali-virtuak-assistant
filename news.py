import requests
from bs4 import BeautifulSoup

#url : kantipur ko website

url = 'https://ekantipur.com/'

response = requests.get(url)
print(response)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h1', class_='')
    articles = soup.find_all('p',id = 4,)
    print('Headline:')
    for headline in headlines:
        print(headline.get_text(strip=True))
    print('Article')
    for article in articles:
        print(article.get_text(strip=True))
else:
    print("failed")



1