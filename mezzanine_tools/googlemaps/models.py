from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import RichText
from mezzanine.pages.models import Page


class Coord(models.Model):
    lat = models.FloatField(_("Latitude"))
    long = models.FloatField(_("Longitude"))

    class Meta:
        abstract = True


class GoogleMap(Page, Coord, RichText):
    zoom = models.PositiveSmallIntegerField(_("Zoom"), default=4)
    map_before_text = models.BooleanField(_("Map before text"), default=False)

    class Meta:
        verbose_name = _('Google map')
        verbose_name_plural = _("Google maps")


class Marker(Coord, RichText):
    map = models.ForeignKey(GoogleMap)
    title = models.CharField(_("Title"), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _("Marker")
        verbose_name_plural = _("Markers")