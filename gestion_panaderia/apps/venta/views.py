from django.shortcuts import render, redirect
from django.urls import reverse

from apps.venta.forms import NuevaVentaForm, ItemFormSet


# Create your views here.

def nueva_venta(request):
    venta_nueva = None
    if request.method == 'POST':
        venta_form = NuevaVentaForm(request.POST) #request.post es un objeto del tipo diccionario
        if venta_form.is_valid():
            venta = venta_form.save()
            formset = ItemFormSet(request.POST, instance=venta)
            if formset.is_valid():
                # Guardar cada item individualmente
                items = formset.save(commit=False)
                for item in items:
                    # Calcular el precio del item basado en la cantidad y el precio del producto
                    item.venta = venta
                    if item.producto:
                        item.precio_item = item.cantidad * item.producto.precio
                    item.save()
                return redirect('venta:lista_ventas')  # Redirige a la lista de ventas después de guardar los items

    else:
        form = NuevaVentaForm()
        formset = ItemFormSet()

    return render(request, 'venta/venta_form.html', {
        'form': form,
        'formset': formset
    })
