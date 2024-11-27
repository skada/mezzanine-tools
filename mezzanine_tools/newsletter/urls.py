from django.urls import path

from mezzanine_tools.newsletter import views as newsletter_views

app_name = "newsletter"

urlpatterns = [
    path("register/", newsletter_views.register, name="register"),
    path("unregister/", newsletter_views.unregister, name="unregister"),
    path("activate/<code>/", newsletter_views.activate, name="activate"),
]
