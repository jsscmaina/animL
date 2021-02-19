from modeltranslation.translator import translator, TranslationOptions
from .models import Guide


class GuideTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


translator.register(Guide, GuideTranslationOptions)
