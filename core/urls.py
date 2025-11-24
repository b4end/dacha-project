from django.urls import path
from . import views

urlpatterns = [
    # Пустая строка '' означает корень поселка (например, zapovednoe/)
    path('', views.index, name='index'),
]