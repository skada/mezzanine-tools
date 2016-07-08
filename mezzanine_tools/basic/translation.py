from mezzanine.pages.translation import TranslationOptions
from modeltranslation.translator import translator

from mezzanine_tools.basic.models import ArticleImage


translator.register(ArticleImage, TranslationOptions)
