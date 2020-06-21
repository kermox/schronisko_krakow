from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'news/news-list.html'
    paginate_by = 15


class PostDetailView(DetailView):
    model = Post
    template_name = 'news/news-detail.html'
