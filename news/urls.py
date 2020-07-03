from django.urls import path
from .views import PostListView, PostDetailView, FacebookPostsUpdate

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('redirect', FacebookPostsUpdate.as_view(),
         name='get-facebook-post'),
]
