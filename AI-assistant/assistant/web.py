# assistant/web.py

import os
import webbrowser
import wikipedia
from config import CHROME_PATH, ANDROID_STUDIO_PATH

def open_application(app):
    paths = {
        "chrome": CHROME_PATH,
        "android studio": ANDROID_STUDIO_PATH
    }
    path = paths.get(app)
    if path and os.path.exists(path):
        os.startfile(path)
        return f"Opening {app}."
    else:
        return f"Path for {app} not found."

def open_website(site):
    url = f"https://{site}.com"
    webbrowser.open_new_tab(url)
    return f"Opening {site}."

def search_wikipedia(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        return f"According to Wikipedia: {summary}"
    except Exception:
        return "Sorry, I couldn't find information on Wikipedia."

def google_search(query):
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open_new_tab(url)
    return "Here are the search results."
