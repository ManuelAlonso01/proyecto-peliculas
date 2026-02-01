from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("subir/", views.subir, name="subir"),
    path("resumen/", views.resumen, name="resumen"),
    path("editar/<int:id_pelicula>", views.editar, name="editar"),
]