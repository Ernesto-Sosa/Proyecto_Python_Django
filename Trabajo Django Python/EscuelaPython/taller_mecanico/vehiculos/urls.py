from django.urls import path
from .views import lista_mecanicos, agregar_mecanico, editar_mecanico, eliminar_mecanico

urlpatterns = [
    path('', lista_mecanicos, name='lista_mecanicos'),
    path('agregar/', agregar_mecanico, name='agregar_mecanico'),
    path('editar/<int:pk>/', editar_mecanico, name='editar_mecanico'),
    path('eliminar/<int:pk>/', eliminar_mecanico, name='eliminar_mecanico'),
]
