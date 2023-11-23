from django.urls import path
from . import views

urlpatterns = [
    path('quiz', views.all_quiz_view, name='quiz'),
    path('search/<str:category>', views.search_view, name='search'),
    path('singlequiz/<int:quiz_id>', views.quiz_view, name='singlequiz'),
]