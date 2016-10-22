from __future__ import unicode_literals

from string import punctuation

from django.db import models
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import FileField
from mezzanine.core.models import Orderable
from mezzanine.pages.models import RichTextPage, Page
from mezzanine.utils.models import upload_to


# class RelatedPagesMixin(object):
#     related_pages = models.ManyToManyField(
#         Page,
#     )


@python_2_unicode_compatible
class ArticleImage(Orderable):

    article = models.ForeignKey(RichTextPage, related_name="images")
    file = FileField(_("File"), max_length=200, format="Image",
        upload_to=upload_to("article.ArticleImage.file", "articles"))
    description = models.CharField(
        _("Description"), max_length=5000, blank=True,)

    #objects = SearchableManager()
    #search_fields = ("description",)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        """
        If no description is given when created, create one from the
        file name.
        """
        if not self.id and not self.description:
            name = force_text(self.file.name)
            name = name.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            name = name.replace("'", "")
            name = "".join([c if c not in punctuation else " " for c in name])
            # str.title() doesn't deal with unicode very well.
            # http://bugs.python.org/issue6412
            name = "".join([s.upper() if i == 0 or name[i - 1] == " " else s
                            for i, s in enumerate(name)])
            self.description = name
        super(ArticleImage, self).save(*args, **kwargs)


class CategoryPage(Page):

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def get_children(self):
        if not self.pk:
            return []

        if getattr(self, '_children_pages', None):
            return self._children_pages

        self._children_pages = Page.objects.published().filter(parent=self).order_by('_order')
        return self._children_pages
