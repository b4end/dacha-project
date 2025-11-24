from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Settlement, User

@admin.register(Settlement)
class SettlementAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'phone')
    prepopulated_fields = {'slug': ('name',)} # Slug будет заполняться сам при вводе имени

# Регистрируем нашу модель пользователя
admin.site.register(User, UserAdmin)