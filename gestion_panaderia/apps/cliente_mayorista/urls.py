from django.urls import path

from apps.cliente_mayorista import views

app_name = 'clientemayorista'
urlpatterns = [
    path('', views.lista_clientesmayoristas, name='lista_clientesmayoristas'),
    #path('<int:pk>/', views.detalle_anuncio, name='detalle_anuncio'),
    path('nuevo/', views.nuevo_clientemayorista,name='nuevo_clientemayorista'),
    path('editar/<int:pk>/', views.editar_clientemayorista, name='editar_clientemayorista'),
    path('eliminar/', views.eliminar_clientemayorista, name='eliminar_clientemayorista'),
]