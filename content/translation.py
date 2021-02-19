from modeltranslation.translator import translator, TranslationOptions
from .models import Post, Category


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Post, PostTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
