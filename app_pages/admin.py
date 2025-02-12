from django.contrib import admin

from app_pages.models import ContactModel


@admin.register(ContactModel)
class BlogsTagModelAdmin(admin.ModelAdmin):
    list_display = ['full_name','subject']
    search_fields = ['subject']
    list_filter = ['full_name']
