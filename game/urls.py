from django.urls import path
from . import views

urlpatterns = [
    path('gamezone',views.game_view, name='gamezone'),
]