from django.contrib import admin


from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(BlogsCategoryModel)
class BlogsCategoryModelAdmin(MyTranslationAdmin):
    list_display = ('title', 'parent')
    search_fields = ('title',)
    list_filter = ('parent', )

@admin.register(BlogsTagModel)
class BlogsTagModelAdmin(MyTranslationAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(BlogsAuthorModel)
class BlogsAuthorModelAdmin(MyTranslationAdmin):
    list_display = ('avatar',)
    search_fields = ('first_name', 'last_name')
    list_filter = ('last_name',)

@admin.register(BlogsModel)
class BlogsModelAdmin(MyTranslationAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    filter_horizontal = ('author', 'categories')

@admin.register(BlogsCommentModel)
class BlogsCommentModelAdmin(MyTranslationAdmin):
    list_display = ('comment', 'user')
    search_fields = ('comment', 'user__username')
    list_filter = ('comment',)

