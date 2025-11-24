from django.shortcuts import render, get_object_or_404
from .models import Settlement

def index(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    context = {
        'settlement': current_settlement,
        'page_title': f"Главная - {current_settlement.name}"
    }
    return render(request, 'core/index.html', context)

def about(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    context = {
        'settlement': current_settlement,
        'page_title': "О поселке"
    }
    return render(request, 'core/about.html', context)

def contacts(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    context = {
        'settlement': current_settlement,
        'page_title': "Контакты"
    }
    return render(request, 'core/contacts.html', context)