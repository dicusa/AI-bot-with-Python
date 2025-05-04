from newsapi import NewsApiClient
from config import NEWS_API_KEY  # add NEWS_API_KEY in config.py

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def get_top_headlines(topic: str = None, country: str = 'us') -> str:
    try:
        if topic:
            articles = newsapi.get_top_headlines(q=topic, language='en', country=country)
        else:
            articles = newsapi.get_top_headlines(language='en', country=country)
        headlines = articles.get('articles', [])
        if not headlines:
            return "Sorry, no news found."
        # Return top 3 headlines
        top_headlines = [f"{i+1}. {item['title']}" for i, item in enumerate(headlines[:3])]
        return "Here are the top news headlines:\n" + "\n".join(top_headlines)
    except Exception:
        return "Sorry, I couldn't fetch news right now."
