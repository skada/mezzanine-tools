from django.conf.urls import url, include
from django.conf.urls import path

urlpatterns = [
    # Cartridge URLs.
    path("reservation_send/", "mezzanine_tools.basic.views.reservation_send", name="reservation_send")
]