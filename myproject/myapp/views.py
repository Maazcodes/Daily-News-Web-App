from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import json
from decouple import config
# Create your views here.


def home(request):
    d = {'articles':[{'title':"news title", 'description':"news description", 'content':"news content"}, {'title':"news title2", 'description':"news description2", 'content':"news content2"}, {'title':"news title3", 'description':"news description3", 'content':"news content3"}]}
    main_content = d['articles']
    titles = [(i['title'], i['description'], i['content']) for i in main_content]
    my_context = {'my_content':titles}
    return render(request, 'home.html', my_context)

def news(request, news_category):
    try:
        context = {'sports_titles':conversion(news_category), 'category':news_category}
        return render(request, 'news.html', context)
    except:
        print("There was a problem accessing the equipment data.")
        return HttpResponse("<h2>Server Issue</h2>")

def conversion(news_category):
    api_key = config('API_KEY')
    url = f"https://newsapi.org/v2/top-headlines?country=in&category={news_category}&apiKey={api_key}"
    news = requests.get(url).text
    news_dict = json.loads(news) # converting json data into Python object to access data
    articles = news_dict['articles']
    # storing title, content, Image URL and main URL of each news item in variable title_list
    title_list = [(article['title'], article['content'], article['urlToImage'], article['url']) for article in articles]
    return title_list
 


