from mezzanine.conf import register_setting
from django.utils.translation import ugettext_lazy as _

register_setting(
    name="RESERV_EMAIL_FROM",
    description=_("Email from which reservation email will come from."),
    editable=True,
    default="",
)

register_setting(
    name="RESERV_EMAIL_TO",
    description=_("Email to which reservation email will be send to."),
    editable=True,
    default="",
)