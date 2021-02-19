from modeltranslation.translator import translator, TranslationOptions
from .models import Front


class FrontTranslationOptions(TranslationOptions):
    fields = ('banner', 'first_title', 'first_box', 'second_title', 'second_box')


translator.register(Front, FrontTranslationOptions)
