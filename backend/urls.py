from django.urls import path
from . import views
urlpatterns=[
    path("loginrestaurante",views.loginRestaurante),
    path("platos_10/listar", views.obtenerPlatos_10),
    path("categorias_10/listar",views.ObtenerCategorias_10),
    path("obtener_restaurantes",views.obtener_restaurantes),
    path("ObtenerPedidos_8/listar",views.ObtenerPedidos_8),
    path("listado", views.ObtenerListado),
    path("recomendaciones", views.ObtenerRecomendaciones),
    path("Cliente", views.loginCliente),
    path("ofertas", views.obtener_ofertas),
    path("ObtenerPedido_Estado_14/listar", views.ObtenerPedido_Estado_14),
    path("ObtenerPedido_Registrar_7/listar",views.ObtenerPedido_Registrar_7),
    path("cambiarestado", views.cambiarEstado),
    path("registrarentrega", views.registrarentrega),
]