from django.shortcuts import render, redirect, get_object_or_404
from .models import Mecanico
from .forms import MecanicoForm

def lista_mecanicos(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'vehiculos/lista_mecanicos.html', {'mecanicos': mecanicos})

def agregar_mecanico(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mecanicos')
    else:
        form = MecanicoForm()
    return render(request, 'vehiculos/agregar_mecanico.html', {'form': form})

def editar_mecanico(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        form = MecanicoForm(request.POST, instance=mecanico)
        if form.is_valid():
            form.save()
            return redirect('lista_mecanicos')
    else:
        form = MecanicoForm(instance=mecanico)
    return render(request, 'vehiculos/editar_mecanico.html', {'form': form})

def eliminar_mecanico(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        mecanico.delete()
        return redirect('lista_mecanicos')
    return render(request, 'vehiculos/eliminar_mecanico.html', {'mecanico': mecanico})
