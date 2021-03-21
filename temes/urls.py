from django.urls import path
from temes import views

app_name = 'temes'

urlpatterns = [
    path('', views.temes, name='temes'),
    path('exercicis/<int:id>', views.exercicis, name='exercicis'),
    path("exercicis/exercici_numero=<int:pk>", views.show_exercici, name='show')
]