import requests

def fetch_news(api_key, query):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'apiKey': api_key,
        'language': 'ne',  # Specify Nepali language
        'pageSize': 5  # Limit the number of articles to 5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        news_data = response.json()
        if 'articles' in news_data and len(news_data['articles']) > 0:
            articles = news_data['articles']
            for article in articles:
                print(f"Title: {article.get('title', 'N/A')}")
                print(f"Description: {article.get('description', 'N/A')}")
                print(f"URL: {article.get('url', 'N/A')}")
                print('-' * 80)
        else:
            print("No articles found.")
    else:
        print("Failed to fetch news data. Status code:", response.status_code)

if __name__ == "__main__":
    api_key = 'e9a2e6d96b394574b3a5f77c6414fb95'
    query = 'नेपाल'
    fetch_news(api_key, query)
