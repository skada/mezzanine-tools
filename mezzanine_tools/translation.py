from modeltranslation.translator import translator

from mezzanine.pages.translation import TranslationOptions

from mezzanine_tools.models import ArticleImage


translator.register(ArticleImage, TranslationOptions)
