from django.contrib import admin

from mails.models import EmailAddress, EmailTemplate


class EmailTemplateAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        has_permission = super(EmailTemplateAdmin, self).has_add_permission(request)

        # Check for the user permission and object instance.
        if has_permission and EmailTemplate.objects.exists():
            # If user has permission and there is already an instance in database,
            # set the permission to False
            has_permission = False
        return has_permission


class EmailAddressAdmin(admin.ModelAdmin):
    search_fields = ['address', ]
    readonly_fields = ['address', ]
    date_hierarchy = 'created_at'


    def has_change_permission(self, request, obj=None):
        has_permission = super(EmailAddressAdmin, self).has_change_permission(request)
        if has_permission:
            has_permission = False
        return has_permission


admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(EmailAddress, EmailAddressAdmin)
