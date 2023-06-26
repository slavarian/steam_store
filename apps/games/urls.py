from django.urls import path

from .views import index, random , about , rounds , render_test , info_steam

urlpatterns = [
    path('main/',index),
    path('random/',random),
    path('about/',about),
    path('round/',rounds),
    path('render/',render_test),
    path('info/',info_steam)  
]