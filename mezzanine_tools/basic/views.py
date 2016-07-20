from django.http import Http404, HttpResponse
from mezzanine.conf import settings
from django.shortcuts import render
from mezzanine.utils.email import send_mail_template


def reservation_send(request):
    if not request.is_ajax():
        raise Http404()

    if request.method != 'POST':
        raise Http404()

    f = settings.RESERV_EMAIL_FROM
    t = settings.RESERV_EMAIL_TO
    if f and t:
        C = {
            'message': "Reservation request raised",
            'fields': []
        }

        for k, v in request.POST.iteritems():
            if k != 'csrfmiddlewaretoken':
                C['fields'].append((k,v,))

        print C

        send_mail_template(
            addr_from=f,
            addr_to=[t, ],
            template='email/form_response',
            subject="T",
            context=C,
        )

    return HttpResponse("test")
