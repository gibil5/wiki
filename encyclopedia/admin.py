from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    #list_display = ("id", "origin", "destination", "duration")
    list_display = ("id", "name", "title", "content")
    #filter_horizontal = ("flights", )

#admin.site.register(Page)
admin.site.register(Page, PageAdmin)
