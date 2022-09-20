from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import *


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'show_logo', 'show_icon']

    def show_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50px"/>'.format(obj.logo.url))
    show_logo.short_description = 'logo'
    def show_icon(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50px"/>'.format(obj.favicon.url))
    show_icon.short_description = 'icon'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'show_image']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'subtitle']


    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50px"/>'.format(obj.image.url))
    show_image.short_description = 'image'