from django.shortcuts import render, get_object_or_404
from core.models import Settlement
from .models import Plot

def plot_list(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    
    # Фильтруем участки только этого поселка
    plots = Plot.objects.filter(settlement=current_settlement)

    context = {
        'settlement': current_settlement,
        'plots': plots,
        'page_title': f"Участки - {current_settlement.name}"
    }
    return render(request, 'realty/plot_list.html', context)