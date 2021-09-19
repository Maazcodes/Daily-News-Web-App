from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('news/<slug:news_category>/', views.news, name="news"),
    # path('health/', views.health, name="health"),
    # path('entertainment/', views.entertainment, name="entertainment"),
    # path('business/', views.business, name="business"),
    # path('technology/', views.technology, name="technology"),
    # path('science/', views.science, name="science"),
]