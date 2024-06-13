from django.shortcuts import render,redirect
from .forms import CalificacionForm
from django.http import HttpRequest
from .models import Alumno, Profesor,Materia,Calificacion
def pagina_principal(request):
    return render(request, 'main.html')

def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})

def profesores(request):
    profesores =  Profesor.objects.all()
    return render(request, 'profesores.html', {'profesores': profesores})
def profesores_subir(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subir')  # Redirige a la página de profesores después de agregar la calificación
    else:
        form = CalificacionForm()
    return render(request, 'subir.html', {'form': form})
def mostra_cal(request):
    calificaciones = Calificacion.objects.all()
    return render(request,'mostrar_cal.html',{'calificaciones': calificaciones})
    