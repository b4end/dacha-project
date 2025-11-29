from django.contrib import admin
from .models import Plot

@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    # Какие поля показывать в списке
    list_display = ('number', 'settlement', 'area', 'price', 'status')
    # Фильтры справа (по поселку и статусу)
    list_filter = ('settlement', 'status')
    # Поиск по номеру участка
    search_fields = ('number',)
    # Возможность редактировать статус прямо из списка (удобно)
    list_editable = ('status', 'price')