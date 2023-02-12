from django.urls import path
from . import views
urlpatterns=[
    path("loginrestaurante",views.loginRestaurante),
    path("platos_10/listar", views.obtenerPlatos_10),
    path("categorias_10/listar",views.ObtenerCategorias_10)
]