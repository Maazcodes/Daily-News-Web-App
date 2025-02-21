from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('news/<slug:news_category>/', views.read_news_with_category, name="news"),
]