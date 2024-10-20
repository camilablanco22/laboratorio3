from django.urls import path

from apps.producto import views

app_name = 'producto'
urlpatterns = [
    #path('', views.lista_anuncios, name='lista_anuncios'),
    #path('<int:pk>/', views.detalle_anuncio, name='detalle_anuncio'),
    path('nuevo/',views.nuevo_producto,name='nuevo_producto'),
    #path('modificar/<int:pk>/', views.editar_anuncio, name='editar_anuncio'),
    #path('eliminar/', views.eliminar_anuncio, name='eliminar_anuncio' )
]