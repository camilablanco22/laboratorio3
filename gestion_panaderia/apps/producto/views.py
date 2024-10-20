from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.producto.forms import NuevoProductoForm


# Create your views here.


def nuevo_producto(request):
    nuevo_prod = None
    if request.method == 'POST':
        producto_form = NuevoProductoForm(request.POST) #request.post es un objeto del tipo diccionario
        if producto_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nuevo_prod = producto_form.save(commit=False)
            nuevo_prod.save()
            #messages.success(request,
             #                'Se ha agregado correctamente el Anuncio {}'.format(nuevo_anuncio))
            return redirect(reverse('producto:listado_productos'))

    else:
        producto_form = NuevoProductoForm()

    return render(request, 'producto/nuevo_producto_form.html', {'form': producto_form})
