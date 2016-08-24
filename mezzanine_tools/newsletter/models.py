from __future__ import unicode_literals

from datetime import timedelta
from uuid import uuid4

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone
from mezzanine.core.models import SiteRelated
from mezzanine.conf import settings


class NewsletterManager(models.Manager):

    def get_by_code(self, code):
        now = timezone.now()
        deadline = now - timedelta(days=settings.NEWSLETTER_TIMEOUT)
        print deadline
        queryset = self.filter(updated__gte=deadline).get(code=code)
        return queryset

    def get_validated(self):
        return self.filter(
            active=True,
            validated=True,
        )


class Newsletter(SiteRelated):
    email = models.EmailField(_('Email'), unique=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True, editable=False)
    updated = models.DateTimeField(_('Updated'), auto_now=True, editable=False)
    active = models.BooleanField(_('Active'), default=True)
    validated = models.BooleanField(_('Validated'), default=False)
    code = models.UUIDField(_('Code'), db_index=True, unique=True, editable=False)

    objects = NewsletterManager()

    def get_new_uuid(self):
        uuid = uuid4()
        return uuid

    def get_activation_url(self):
        url = reverse("newsletter:activate", kwargs={'code': self.code.hex, })
        return url

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.get_new_uuid()
        super(Newsletter, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Newsletter')
        verbose_name_plural = _('Newsletter')
