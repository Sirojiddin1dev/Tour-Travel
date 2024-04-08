from modeltranslation.translator import register, TranslationOptions, translator
from .models import *


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text', )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'text', )


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
