from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from apps.cliente_mayorista.models import ClienteMayorista
from apps.cliente_mayorista.forms import NuevoClienteMayoristaForm, ModificarClienteMayoristaForm



# Create your views here.
def lista_clientesmayoristas(request):
    clientemayorista = ClienteMayorista.objects.all()
    return render(request, 'clientemayorista/lista_clientesmayoristas.html', {'clientemayorista': clientemayorista})






def nuevo_clientemayorista(request):
    nuevo_clientem = None
    if request.method == 'POST':
        clientemayorista_form = NuevoClienteMayoristaForm(request.POST) #request.post es un objeto del tipo diccionario
        if clientemayorista_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nuevo_clientem = clientemayorista_form.save(commit=False)
            nuevo_clientem.save()
            #messages.success(request,
             #                'Se ha agregado correctamente el Anuncio {}'.format(nuevo_anuncio))
            return redirect(reverse('clientemayorista:lista_clientesmayoristas'))
            #return redirect('producto: nuevo_producto')

    else:
        clientemayorista_form = NuevoClienteMayoristaForm()

    return render(request, 'clientemayorista/clientemayorista_form.html', {'form': clientemayorista_form})



def editar_clientemayorista(request, pk):
    clientemayorista = get_object_or_404(ClienteMayorista, pk=pk)
    if request.method == 'POST':
        clientemayorista_form = ModificarClienteMayoristaForm(request.POST, instance=clientemayorista)
        if clientemayorista_form.is_valid():
            clientemayorista_form.save(commit=True)
            messages.success(request, 'Se ha actualizado correctamente el Cliente Mayorista')
            return redirect(reverse('clientemayorista:lista_clientesmayoristas'))
    else:
        clientemayorista_form = ModificarClienteMayoristaForm(instance=clientemayorista)

    return render(request, 'clientemayorista/clientemayorista_form.html', {'form': clientemayorista_form})



def eliminar_clientemayorista(request):
    if request.method == 'POST':
        if 'id_clientemayorista' in request.POST:
            clientemayorista = get_object_or_404(ClienteMayorista, pk=request.POST['id_clientemayorista'])
            nombre_clientemayorista = clientemayorista.nombre_completo
            clientemayorista.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Cliente Mayorista {}'.format(nombre_clientemayorista))
        else:
            messages.error(request, 'Debe indicar cual Cliente Mayorista se desea eliminar')
    return redirect(reverse('clientemayorista:lista_clientesmayoristas'))
