from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('documents/', views.documents_list, name='documents_list'),
    path('infrastructure/', views.render_static_page, {'page_slug': 'infrastructure'}, name='infrastructure'),
    
    # НОВЫЙ МАРШРУТ
    path('gallery/', views.gallery_view, name='gallery'),
]