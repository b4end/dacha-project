from django.contrib import admin
from .models import News, Document, GalleryImage, StaticPage

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'settlement', 'created_at')
    list_filter = ('settlement',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'settlement', 'is_public', 'created_at')
    list_filter = ('settlement', 'is_public')

@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'settlement')
    list_filter = ('settlement',)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'settlement', 'caption')