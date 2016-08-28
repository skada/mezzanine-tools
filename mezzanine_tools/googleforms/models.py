from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import RichText
from mezzanine.pages.models import Page


class GoogleForm(Page, RichText):
    form_url = models.URLField(_("Form URL"))
    form_width = models.SmallIntegerField(_("Width"), null=True, blank=True)
    form_height = models.SmallIntegerField(_("Height"), null=True, blank=True)
    form_before_text = models.BooleanField(_("Map before text"), default=False)

    class Meta:
        verbose_name = _('Google form')
        verbose_name_plural = _("Google forms")
