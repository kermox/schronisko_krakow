from django.core.files import File
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from io import BytesIO
import requests
from PIL import Image

from schronisko_krakow.settings import USER_ACCESS_TOKEN, PAGE_ID
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    template_name = 'posts/post-list.html'
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post-details.html'


class FacebookPostsUpdate(View):

    def get(self, request):
        parameters = {'access_token': USER_ACCESS_TOKEN}
        page_url = f'https://graph.facebook.com/{PAGE_ID}/feed?fields=message,updated_time,picture.width(1000).height(1000)'
        data = requests.get(page_url, params=parameters)
        data_json = data.json()
        local_id_base = [i.facebook_id for i in Post.objects.all()]
        facebook_id_base = [data_json['data'][i]['id']
                            for i in range(0, len(data_json['data']))]

        for i in range(0, len(data_json['data'])):

            if data_json['data'][i]['id'] not in local_id_base:
                facebook_post = Post(
                    title=f"Facebook post: {data_json['data'][i]['message'][0:25]}'",
                    content=data_json['data'][i]['message'],
                    facebook_id=data_json['data'][i]['id'],
                )

                if 'picture' in data_json['data'][i].keys():
                    image = Image.open(requests.get(data_json['data'][i]['picture'], stream=True).raw)
                    blob = BytesIO()
                    image.save(blob, 'JPEG')
                    facebook_post.img.save(f"fb_image_{data_json['data'][i]['id']}.jpg", File(blob), save=False)
                facebook_post.save()

        for i in local_id_base:
            if Post.objects.get(facebook_id=i).facebook_id not in facebook_id_base:
                Post.objects.filter(facebook_id=i).delete()

        return redirect('admin:news_post_changelist')
