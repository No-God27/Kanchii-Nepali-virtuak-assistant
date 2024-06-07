import requests

def fetch_news(api_key, query):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    api_key = 'e9a2e6d96b394574b3a5f77c6414fb95'
    query = 'नेपाल'
    news = fetch_news(api_key, query)


    print(news)

    if 'articles' in news:
        for article in news['articles']:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print('-' * 80)
    else:
        print("No articles found.")
