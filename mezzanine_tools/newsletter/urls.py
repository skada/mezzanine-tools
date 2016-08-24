from __future__ import unicode_literals

from django.conf.urls import url

from mezzanine_tools.newsletter import views as newsletter_views

app_name = "newsletter"

urlpatterns = [
    url("^register/$", newsletter_views.register, name="register"),
    url("^unregister/$", newsletter_views.unregister, name="unregister"),
    url("^activate/(?P<code>[\w-]+)/$", newsletter_views.activate, name="activate"),
]
