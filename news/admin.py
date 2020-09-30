from django.contrib import admin
from news.models import Post, FacebookPost


class PostAdmin(admin.ModelAdmin):
    pass


class FacebookPostAdmin(admin.ModelAdmin):
    change_list_template = 'admin/posts/change_list.html'


admin.site.register(Post, PostAdmin)
admin.site.register(FacebookPost, FacebookPostAdmin)