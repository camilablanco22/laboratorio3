# apps/materia_prima/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from apps.pedido.forms import NuevaMateriaPrimaForm, ModificarMateriaPrimaForm
from apps.pedido.models import MateriaPrima

def lista_materia_prima(request):
    materia_prima = MateriaPrima.objects.all()
    return render(request, 'pedido/lista_materia_prima.html', {'materia_prima': materia_prima})

def nueva_materia_prima(request):
    if request.method == 'POST':
        form = NuevaMateriaPrimaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pedido:lista_materia_prima'))
    else:
        form = NuevaMateriaPrimaForm()
    return render(request, 'pedido/materia_prima_form.html', {'form': form})

def editar_materia_prima(request, pk):
    materia = get_object_or_404(MateriaPrima, pk=pk)
    if request.method == 'POST':
        form = ModificarMateriaPrimaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Materia Prima actualizada correctamente')
            return redirect(reverse('pedido:lista_materia_prima'))
    else:
        form = ModificarMateriaPrimaForm(instance=materia)
    return render(request, 'pedido/materia_prima_form.html', {'form': form})

def eliminar_materia_prima(request):
    if request.method == 'POST':
        materia_id = request.POST.get('id_materia')
        materia = get_object_or_404(MateriaPrima, pk=materia_id)
        nombre_materia = materia.nombre
        materia.delete()
        messages.success(request, f'Se ha eliminado {nombre_materia} exitosamente')
    return redirect(reverse('pedido:lista_materia_prima'))

