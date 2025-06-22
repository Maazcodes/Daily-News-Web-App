from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import json
import os

# https://docs.python.org/3/library/json.html
# This library will be used to parse the JSON data returned by the API.

# https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# This library will be used to fetch the API.
import urllib.request

apikey = os.environ.get('API_KEY')
# apikey = "f8f45c001685907fcfcf2de832c0ae89"


def home(request):
   
    return render(request, 'home.html')

def read_news_with_category(request, news_category):
    try:
        context = {'sports_titles':read_news(news_category), 'category':news_category}
        return render(request, 'news.html', context)
    except:
        print("There was a problem accessing the equipment data.")
        return HttpResponse("<h2>Server Issue</h2>")

def read_news(news_category):
    # api_key = '509fadfddd8543bc89459c4b05f7c20d'
    # url = f"https://newsapi.org/v2/top-headlines?country=us&category={news_category}&apiKey={api_key}"
    url = f"https://gnews.io/api/v4/search?q={news_category}&lang=en&country=us&max=10&apikey={apikey}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]
    # news = requests.get(url).text
    # news_dict = json.loads(news) # converting json data into Python object to access data
    # articles = news_dict['articles']
    # storing title, content, Image URL and main URL of each news item in variable title_list
        title_list = [(article['title'], article['content'], article['image'], article['url']) for article in articles]
        return title_list
 


