from django.shortcuts import render, get_object_or_404
from .models import Settlement

def index(request, settlement_slug):
    # Ищем поселок в БД. Если нет такого (например /test/), выдаст 404 ошибку
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    
    context = {
        'settlement': current_settlement,
        'page_title': f"Главная - {current_settlement.name}"
    }
    return render(request, 'core/index.html', context)