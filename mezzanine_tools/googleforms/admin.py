import copy

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.admin import PageAdmin
from mezzanine_tools.googleforms.models import GoogleForm

googlemap_fieldsets = list(copy.deepcopy(PageAdmin.fieldsets))
googlemap_fieldsets[0][1]['fields'].insert(3, 'content')
googlemap_fieldsets[0][1]['fields'].insert(4, 'form_before_text')
googlemap_fieldsets.insert(1, (
    _("Google form"),
    {
        "fields": [
            'form_url',
            ('form_width', 'form_height'),
        ]
    }
))


class GoogleFormAdmin(PageAdmin):
    fieldsets = googlemap_fieldsets

    radio_fields = {"status": admin.HORIZONTAL}


admin.site.register(GoogleForm, GoogleFormAdmin)
