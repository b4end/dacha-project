from django.urls import path
from . import views

urlpatterns = [
    # Список участков
    path('', views.plot_list, name='plot_list'),
]