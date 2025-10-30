from django.shortcuts import render, get_object_or_404, redirect
from .models import Miembro, Membresia # Importa Membresia
from .forms import MiembroForm

# Vistas para Miembros
def listar_miembros(request):
    miembros = Miembro.objects.all()
    return render(request, 'listar_miembros.html', {'miembros': miembros})

def detalle_miembro(request, id_miembro):
    miembro = get_object_or_404(Miembro, id_miembro=id_miembro)
    return render(request, 'detalle_miembro.html', {'miembro': miembro})

def crear_miembro(request):
    if request.method == 'POST':
        form = MiembroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_gym:listar_miembros') # Redirige a la lista
        else:
            # Si el formulario no es válido, vuelve a mostrarlo con errores
            print(form.errors) # Esto es útil para depurar
    else:
        form = MiembroForm()
    return render(request, 'formulario_miembro.html', {'form': form, 'titulo': 'Registrar Miembro'})

def editar_miembro(request, id_miembro):
    miembro = get_object_or_404(Miembro, id_miembro=id_miembro)
    if request.method == 'POST':
        form = MiembroForm(request.POST, request.FILES, instance=miembro)
        if form.is_valid():
            form.save()
            return redirect('app_gym:detalle_miembro', id_miembro=miembro.id_miembro) # Redirige al detalle
        else:
            print(form.errors) # Depuración
    else:
        form = MiembroForm(instance=miembro)
    return render(request, 'formulario_miembro.html', {'form': form, 'titulo': 'Editar Miembro'})

def borrar_miembro(request, id_miembro):
    miembro = get_object_or_404(Miembro, id_miembro=id_miembro)
    if request.method == 'POST':
        miembro.delete()
        return redirect('app_gym:listar_miembros') # Redirige a la lista
    return render(request, 'confirmar_borrar_miembro.html', {'miembro': miembro})