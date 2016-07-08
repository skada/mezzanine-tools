from __future__ import unicode_literals

from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    name = 'newsletter'

    def ready(self):
        import mezzanine_tools.newsletter.defaults
