import requests

def fetchnews(apikey, query):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'apiKey': apikey
    }
    response = requests.get(url, params=params)
    return response.json()

if _name == "__main":
    api_key = 'e9a2e6d96b394574b3a5f77c6414fb95'  # Replace with your NewsAPI API key
    query = 'नेपाल'  # Example query in Nepali
    news = fetch_news(api_key, query)

    # Print the full response for debugging
    print(news)

    if 'articles' in news:
        for article in news['articles']:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print('-' * 80)
    else:
        print("No articles found.")