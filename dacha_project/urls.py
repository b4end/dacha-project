from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def root_redirect(request):
    return redirect('/zapovednoe/', permanent=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_redirect),

    path('<slug:settlement_slug>/realty/', include('realty.urls')),
    
    # Подключаем content.urls. Все пути внутри будут начинаться с /info/
    # Например: /zapovednoe/info/news/ или /zapovednoe/info/documents/
    path('<slug:settlement_slug>/info/', include('content.urls')),

    path('<slug:settlement_slug>/', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)