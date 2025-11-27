from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Функция-заглушка для главной страницы
def root_redirect(request):
    return redirect('/zapovednoe/', permanent=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Редирект с пустого пути
    path('', root_redirect),

    # 1. Подключаем приложение Realty (Участки)
    # Ссылка будет вида: /zapovednoe/realty/
    path('<slug:settlement_slug>/realty/', include('realty.urls')),

    # 2. Подключаем приложение Core (Главная, О нас, Контакты)
    # ВАЖНО: Эта строка должна быть ПОСЛЕДНЕЙ из динамических, 
    # так как она ловит "пустой" хвост (например /zapovednoe/).
    path('<slug:settlement_slug>/', include('core.urls')),
]