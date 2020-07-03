from django.contrib import admin
from news.models import Post


class PostAdmin(admin.ModelAdmin):
    change_list_template = 'admin/news/change_list.html'


admin.site.register(Post, PostAdmin)
