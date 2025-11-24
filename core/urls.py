from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Добавь эти две строчки:
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]