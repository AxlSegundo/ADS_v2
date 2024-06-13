from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='main'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('profesores/', views.profesores, name='profesores'),
    path('mostrar/',views.mostra_cal, name='mostrar_cal'),
    path('subir/',views.profesores_subir,name='subir')
]