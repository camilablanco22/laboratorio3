from django.shortcuts import render, redirect
from django.urls import reverse

from apps.venta.forms import NuevaVentaForm


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
            return redirect('venta:carga_items')

    else:
        venta_form = NuevaVentaForm()

    return render(request, 'venta/venta_form.html', {'form': venta_form})