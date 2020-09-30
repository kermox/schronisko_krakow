from django.contrib import admin
from mails.models import EmailTemplates, EmailBase


class EmailTemplatesAdmin(admin.ModelAdmin):
    pass


class EmailBaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(EmailTemplates, EmailTemplatesAdmin)
admin.site.register(EmailBase, EmailBaseAdmin)


