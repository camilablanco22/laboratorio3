from django.urls import path
from apps.pedido import views

app_name = 'materia_prima'
urlpatterns = [
    path('', views.lista_materia_prima, name='lista_materia_prima'),
    path('nuevo/', views.nueva_materia_prima, name='nueva_materia_prima'),
    path('editar/<int:pk>/', views.editar_materia_prima, name='editar_materia_prima'),
    path('eliminar/', views.eliminar_materia_prima, name='eliminar_materia_prima'),
]