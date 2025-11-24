from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Функция-заглушка для главной страницы
def root_redirect(request):
    # По ТЗ: Главная страница сайта (/) должна перенаправлять на /zapovednoe
    return redirect('/zapovednoe/', permanent=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Редирект с пустого пути
    path('', root_redirect),

    # Динамический путь. <slug:settlement_slug> попадает в views.py
    path('<slug:settlement_slug>/', include('core.urls')),
]