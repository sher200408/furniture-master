from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.BlogsCategoryModel)
class BlogsCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.BlogsTagModel)
class BlogsTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.BlogsAuthorModel)
class BlogsAuthorTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name',)



@register(models.BlogsModel)
class BlogsModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(models.BlogsCommentModel)
class BlogsCommentTranslationOptions(TranslationOptions):
    fields = ('comment',)
