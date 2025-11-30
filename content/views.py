from django.shortcuts import render, get_object_or_404
from core.models import Settlement
from .models import News, Document, StaticPage, GalleryImage

def news_list(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    news = News.objects.filter(settlement=current_settlement)
    
    context = {
        'settlement': current_settlement,
        'news': news,
        'page_title': f"Новости - {current_settlement.name}"
    }
    return render(request, 'content/news_list.html', context)

def news_detail(request, settlement_slug, pk):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    post = get_object_or_404(News, pk=pk, settlement=current_settlement)
    
    context = {
        'settlement': current_settlement,
        'post': post,
        'page_title': post.title
    }
    return render(request, 'content/news_detail.html', context)

def documents_list(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    
    all_docs = Document.objects.filter(settlement=current_settlement)
    visible_docs = []
    user = request.user
    
    for doc in all_docs:
        if doc.is_public:
            visible_docs.append(doc)
        elif user.is_authenticated and (user.is_staff or (user.settlement == current_settlement and user.role != 'guest')):
            visible_docs.append(doc)
            
    context = {
        'settlement': current_settlement,
        'documents': visible_docs,
        'page_title': f"Документы - {current_settlement.name}",
        'is_resident': user.is_authenticated and user.settlement == current_settlement
    }
    return render(request, 'content/documents_list.html', context)

def render_static_page(request, settlement_slug, page_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    page_data = StaticPage.objects.filter(settlement=current_settlement, slug=page_slug).first()
    
    # СЛОВАРЬ ЗАГОЛОВКОВ ПО УМОЛЧАНИЮ
    # Если страницы нет в базе, берем красивое название отсюда
    default_titles = {
        'infrastructure': 'Инфраструктура',
        'about': 'О поселке'
    }
    
    # Определяем заголовок: 
    # 1. Если страница есть в БД -> берем её заголовок
    # 2. Если нет -> берем из словаря
    # 3. Если нет в словаре -> просто "Страница"
    if page_data:
        title = page_data.title
    else:
        base_title = default_titles.get(page_slug, "Страница")
        title = f"{base_title} {current_settlement.name}"

    context = {
        'settlement': current_settlement,
        'page': page_data,
        'page_title': title
    }
    return render(request, 'content/static_page.html', context)

def gallery_view(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    images = GalleryImage.objects.filter(settlement=current_settlement).order_by('-created_at')
    
    context = {
        'settlement': current_settlement,
        'images': images,
        'page_title': f"Галерея - {current_settlement.name}"
    }
    return render(request, 'content/gallery.html', context)