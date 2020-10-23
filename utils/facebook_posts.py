import requests

from news.models import FacebookPost
from schronisko_krakow.settings import PAGE_ID, USER_ACCESS_TOKEN


def get_facebook_posts():
    parameters = {'access_token': USER_ACCESS_TOKEN}
    page_url = f'https://graph.facebook.com/{PAGE_ID}/posts?fields=permalink_url'
    data = requests.get(page_url, params=parameters)
    data_json = data.json()
    local_id_base = [i.facebook_post_id for i in FacebookPost.objects.all()]

    for i in range(0, len(data_json['data'])):
        if data_json['data'][i]['id'] not in local_id_base:
            facebook_post = FacebookPost(
                facebook_permalink_url=data_json['data'][i]['permalink_url'],
                facebook_post_id=data_json['data'][i]['id'],
            )
            facebook_post.save()
