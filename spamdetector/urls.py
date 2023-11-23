from django.urls import path
from . import views

urlpatterns = [
    path('spam/',views.spam_view, name='spam'),
]