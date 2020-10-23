from django.urls import path

from .views import (NewsDetailView, NewsListView, TopicDetailView,
                    update_facebook_posts)

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news-detail'),
    path('topics/<slug:slug>/', TopicDetailView.as_view(), name='news-topic-detail'),
    path('redirect', update_facebook_posts, name='news-update')
]
