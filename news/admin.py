from django.contrib import admin

from news.models import FacebookPost, Post, Topic


class PostAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list.html'
    fields = [('title', 'pinned'), 'content', 'img', 'status', 'topic', ]
    list_display = ['title', 'status', 'pinned', 'topic', ]
    list_editable = ['status', 'pinned']
    list_filter = ['status', 'topic', 'pinned', ]
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'


class FacebookPostAdmin(admin.ModelAdmin):
    change_list_template = 'admin/news/change_list.html'
    fields = ['status']
    list_display = ['__str__', 'status', ]
    list_editable = ['status', ]
    list_filter = ['status', ]


class TopicAdmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list.html'
    fields = ['name', ]
    list_display = ['__str__', 'get_post_display', ]

    def get_post_display(self, obj):
        """
        Returns all posts related to topic.
        """
        return [i.title for i in obj.post_set.all()]

    get_post_display.short_description = 'posty'





admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(FacebookPost, FacebookPostAdmin)