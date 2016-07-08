import copy
import json

from django.core.mail import send_mail
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader
from django.utils.translation import ugettext as _

from mezzanine.conf import settings

from mezzanine_tools.newsletter.models import Newsletter


def register(request):
    if request.method != 'POST':
        raise Http404()
    email = request.POST.get('email')
    newsletter, created = Newsletter.objects.get_or_create(email=email)
    if not created:
        msg = _('Email addressalready registered')
    else:
        t = loader.get_template("newsletter/email/email_confirm.txt")
        c = {
            'newsletter': newsletter
        }
        msg = t.render(context=c,)
        send_mail(
            _("Newsletter confirmaion email"),
            msg,
            settings.NEWSLETTER_FROM,
            [newsletter.email,]
        )
        msg = _('Successfully registered. We have sent you an confirmation email.')

    return render(request, 'newsletter/register.html', {'msg': msg, 'newsletter': newsletter})


def unregister(request, code):
    try:
        newsletter = Newsletter.objects.get(code=code)
        newsletter.active = False
        newsletter.save()
        msg = _('Your newsletter email address have been successfully de-registered.')
    except Newsletter.DoesNotExist:
        msg = _('Unable to de-register the newsletter email. Please contact our support.')
    return render(request, 'newsletter/unregistration_complete.html', {'msg': msg, 'newsletter': newsletter})


def activate(request, code):
    try:
        newsletter = Newsletter.objects.get_by_code(code)
        newsletter.validated = True
        newsletter.active = True
        newsletter.save()
        msg = _('Your newsletter email address have been successfully activated.')
    except Newsletter.DoesNotExist:
        msg = _('Unable to activate the newsletter email. Please contact our support.')
    return render(request, 'newsletter/registration_complete.html.html', {'msg': msg, 'newsletter': newsletter})