from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .models import Settlement
from content.models import StaticPage
from .forms import SignUpForm, UserInfoForm, UserAvatarForm # Импортируем новые формы

def index(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    context = {
        'settlement': current_settlement,
        'page_title': f"Главная - {current_settlement.name}"
    }
    return render(request, 'core/index.html', context)

def about(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    page_data = StaticPage.objects.filter(settlement=current_settlement, slug='about').first()
    
    context = {
        'settlement': current_settlement,
        'page': page_data,
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

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', settlement_slug=user.settlement.slug)
    else:
        form = SignUpForm()
    
    default_settlement = Settlement.objects.first()
    
    context = {
        'form': form,
        'settlement': default_settlement
    }
    return render(request, 'registration/register.html', context)

# --- ОБНОВЛЕННАЯ ФУНКЦИЯ ПРОФИЛЯ ---
def profile(request, settlement_slug):
    current_settlement = get_object_or_404(Settlement, slug=settlement_slug)
    
    info_form = None
    avatar_form = None

    if request.user.is_authenticated:
        # Инициализируем формы текущими данными
        info_form = UserInfoForm(instance=request.user)
        avatar_form = UserAvatarForm(instance=request.user)

        if request.method == 'POST':
            # Смотрим, какую кнопку нажал пользователь (по скрытому полю action)
            action = request.POST.get('action')

            if action == 'update_info':
                # Обновление текста
                info_form = UserInfoForm(request.POST, instance=request.user)
                if info_form.is_valid():
                    info_form.save()
                    return redirect('profile', settlement_slug=settlement_slug)
            
            elif action == 'update_avatar':
                # Загрузка новой аватарки
                avatar_form = UserAvatarForm(request.POST, request.FILES, instance=request.user)
                if avatar_form.is_valid():
                    avatar_form.save()
                    return redirect('profile', settlement_slug=settlement_slug)

            elif action == 'delete_avatar':
                # Удаление аватарки
                if request.user.avatar:
                    request.user.avatar.delete() # Удаляем файл
                    request.user.avatar = None   # Очищаем поле в БД
                    request.user.save()
                return redirect('profile', settlement_slug=settlement_slug)

    context = {
        'settlement': current_settlement,
        'page_title': "Личный кабинет",
        'info_form': info_form,
        'avatar_form': avatar_form
    }
    return render(request, 'core/profile.html', context)