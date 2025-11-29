from django.urls import path
from . import views

urlpatterns = [
    # Список новостей
    path('news/', views.news_list, name='news_list'),
    
    # --- НОВЫЙ МАРШРУТ (Детальная страница новости) ---
    # <int:pk> означает, что сюда подставится ID новости (1, 2, 5...)
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    
    path('documents/', views.documents_list, name='documents_list'),
    path('infrastructure/', views.render_static_page, {'page_slug': 'infrastructure'}, name='infrastructure'),
]