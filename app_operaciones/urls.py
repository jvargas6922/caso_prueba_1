from django.urls import path, include
from app_operaciones import views
from .import views
urlpatterns = [
    path('crear/', views.crear_procedimiento, name='crear_procedimiento'),
    path('crear_sala/', views.crear_sala, name='crear_sala'),
]
