from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from apps.venta.forms import NuevaVentaForm
from apps.venta.models import Venta, Item


# Create your views here.


def nueva_venta(request):
    venta_nueva = None
    if request.method == 'POST':
        venta_form = NuevaVentaForm(request.POST) #request.post es un objeto del tipo diccionario
        if venta_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            venta_nueva = venta_form.save(commit=False)
            #Lógica para registrar el empleado
            venta_nueva.save()
            #messages.success(request,
             #                'Se ha agregado correctamente el Anuncio {}'.format(nuevo_anuncio))
            return redirect('venta:cargar_items', venta_id=venta_nueva.id)

    else:
        venta_form = NuevaVentaForm()

    return render(request, 'venta/venta_form.html', {'form': venta_form})

def cargar_items(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    ItemFormSet = inlineformset_factory(Venta, Item, fields=('producto', 'cantidad'), extra=1, can_delete=True)

    if request.method == 'POST':
        formset = ItemFormSet(request.POST, instance=venta)
        if formset.is_valid():
            # Guardar cada item individualmente
            items = formset.save(commit=False)
            for item in items:
                # Calcular el precio del item basado en la cantidad y el precio del producto
                if item.producto:
                    item.precio_item = item.cantidad * item.producto.precio
                item.save()

            formset.save_m2m()  # Si hay relaciones ManyToMany
            return redirect('venta:lista_ventas')  # Redirige a la lista de ventas después de guardar los items
    else:
        formset = ItemFormSet(instance=venta)

    return render(request, 'venta/cargar_items.html', {'formset': formset, 'venta': venta})

def lista_ventas(request):
    ventas = Venta.objects.all()  # Obtener todas las ventas
    return render(request, 'venta/lista_ventas.html', {'ventas': ventas})

def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)  # Obtener la venta específica
    items = Item.objects.filter(venta=venta)  # Obtener los items relacionados a esta venta
    return render(request, 'venta/detalle_venta.html', {'venta': venta, 'items': items})