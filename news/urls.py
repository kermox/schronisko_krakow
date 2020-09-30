from django.urls import path
from .views import PostListView, PostDetailView, update_facebook_posts

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('redirect', update_facebook_posts, name='update-posts'),
]
