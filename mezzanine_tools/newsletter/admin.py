from django.contrib import admin

from mezzanine_tools.newsletter.models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'active',
        'validated',
        'created',
        'updated',
        'code',
    )


admin.site.register(Newsletter, NewsletterAdmin)