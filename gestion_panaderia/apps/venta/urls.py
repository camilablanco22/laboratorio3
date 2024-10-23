from django.urls import path
from . import views

app_name = 'venta'

urlpatterns = [
    path('nueva/', views.nueva_venta, name='nueva_venta'),
    path('items/<int:venta_id>/', views.cargar_items, name='cargar_items'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),  # Listar ventas
    path('ventas/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),  # Detalle de venta
]