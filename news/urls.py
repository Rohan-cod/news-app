from django.urls import path

from .views import NewsListView, HomePageView, NewsDetailView, search_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('jobs/', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/',
         NewsDetailView.as_view(), name='news_detail'),
    path('search/', search_view, name='search'),
]