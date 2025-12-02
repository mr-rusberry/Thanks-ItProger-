from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name='news'),
    path('add_news', views.add_news, name='add_news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
]
