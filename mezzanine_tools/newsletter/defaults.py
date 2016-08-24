from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


register_setting(
    name='NEWSLETTER_FROM',
    label=_('An email address to send a newsletter from'),
    default='newsletter@localhost',
    editable=True,
)


register_setting(
    name='NEWSLETTER_TIMEOUT',
    label=_('Newsletter address activation in days'),
    default=7,
    editable=True,
)


