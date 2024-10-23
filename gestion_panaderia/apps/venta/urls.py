from django.urls import path

from apps.venta import views

app_name = 'producto'
urlpatterns = [
    #path('', views.lista_productos, name='lista_productos'),
    #path('<int:pk>/', views.detalle_anuncio, name='detalle_anuncio'),
    path('nueva/',views.nueva_venta,name='nueva_venta'),
    #path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    #path('eliminar/', views.eliminar_producto, name='eliminar_producto' )
]