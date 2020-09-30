import operator
from itertools import chain

from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Post, FacebookPost


class PostListView(ListView):
    model = Post
    template_name = 'posts/post-list.html'
    paginate_by = 10
    extra_context = {
        'post_list_page': 'active'
    }

    def get_queryset(self):
        sorted_combined_list = sorted(chain(Post.objects.filter(status='published'), FacebookPost.objects.filter(status='published')), key=operator.attrgetter('created_at'), reverse=True)
        return sorted_combined_list


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post-details.html'
    context_object_name = 'post'
    extra_context = {
        'post_detail_page': 'active'

    }


def update_facebook_posts(request):
    if request.method == "POST":
        from utils.facebook_posts import get_facebook_posts
        get_facebook_posts()
        return redirect(reverse('admin:news_facebookpost_changelist'))
