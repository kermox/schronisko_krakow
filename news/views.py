from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'news/news.html'
    paginate_by = 15
