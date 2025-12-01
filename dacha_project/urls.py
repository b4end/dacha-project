from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views

def root_redirect(request):
    return redirect('/zapovednoe/', permanent=False)

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- АВТОРИЗАЦИЯ ---
    path('register/', core_views.register, name='register'),

    # ИЗМЕНЕНИЕ: Сначала ставим наш кастомный вход
    path('accounts/login/', core_views.CustomLoginView.as_view(), name='login'),

    # Потом подключаем остальные стандартные пути (logout, password_reset и т.д.)
    path('accounts/', include('django.contrib.auth.urls')),
    # -------------------

    path('', root_redirect),

    path('<slug:settlement_slug>/realty/', include('realty.urls')),
    path('<slug:settlement_slug>/info/', include('content.urls')),
    path('<slug:settlement_slug>/', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)