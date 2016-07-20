from django.conf.urls import url, include

urlpatterns = [

    # Cartridge URLs.
    url(r"^reservation_send/", "mezzanine_tools.basic.views.reservation_send", name="reservation_send")
]