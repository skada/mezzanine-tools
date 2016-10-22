from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage

from mezzanine_tools.basic.models import ArticleImage, CategoryPage


class GalleryImageInline(TabularDynamicInlineAdmin):
    classes = ('collapse-open',)
    model = ArticleImage


class ArticleAdmin(PageAdmin):
    inlines = [GalleryImageInline, ]


@admin.register(CategoryPage)
class CategoryAdmin(PageAdmin):
    pass

admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, ArticleAdmin)

