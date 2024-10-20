from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.producto.forms import NuevoProductoForm, ModificarProductoForm
from apps.producto.models import Producto


# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/lista_productos.html', {'productos': productos})






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
            return redirect(reverse('producto:lista_productos'))
            #return redirect('producto: nuevo_producto')

    else:
        producto_form = NuevoProductoForm()

    return render(request, 'producto/producto_form.html', {'form': producto_form})



def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto_form = ModificarProductoForm(request.POST, instance=producto)
        if producto_form.is_valid():
            producto_form.save(commit=True)
            messages.success(request, 'Se ha actualizado correctamente el Producto')
            return redirect(reverse('producto:lista_productos'))
    else:
        producto_form = ModificarProductoForm(instance=producto)

    return render(request, 'producto/producto_form.html', {'form': producto_form})