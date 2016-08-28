import copy

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.admin import TabularDynamicInlineAdmin, StackedDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from mezzanine_tools.googlemaps.models import GoogleMap, Marker


class MarkerInline(StackedDynamicInlineAdmin):
    model = Marker
    fields = (('title', 'lat', 'long'), 'content')


googlemap_fieldsets = list(copy.deepcopy(PageAdmin.fieldsets))
googlemap_fieldsets[0][1]['fields'].insert(3, 'content')
googlemap_fieldsets[0][1]['fields'].insert(4, 'map_before_text')
googlemap_fieldsets.insert(1, (
    _("Google map"),
    {
        "fields": [
            ('lat', 'long'),
            'zoom',
        ]
    }
))

class GoogleMapAdmin(PageAdmin):
    fieldsets = googlemap_fieldsets
    inlines = (MarkerInline, )

    radio_fields = {"status": admin.HORIZONTAL}


admin.site.register(GoogleMap, GoogleMapAdmin)
