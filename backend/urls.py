from django.urls import path
from . import views
urlpatterns=[
    path("loginrestaurante",views.loginRestaurante),
    path("platos_10/listar", views.obtenerPlatos_10),
    path("platos_1000/listar", views.obtenerPlatos_1000),
    path("categorias_10/listar",views.ObtenerCategorias_10),
    path("obtener_restaurantes",views.obtener_restaurantes),
    path("ObtenerPedidos_8/listar",views.ObtenerPedidos_8),
    path("listado", views.ObtenerListado),
    path("recomendaciones", views.ObtenerRecomendaciones),
    path("Cliente", views.loginCliente),
    path("ofertas", views.obtener_ofertas),
    path("ObtenerPedido_Estado_14/listar", views.ObtenerPedido_Estado_14),
    path("ObtenerPedido_Registrar_7/listar",views.ObtenerPedido_Registrar_7),
    path("ObtenerSoloRestaurante_7/listar",views.ObtenerSoloRestaurante_7),
    path("ObtenerSoloCliente_7/listar",views.ObtenerSoloCliente_7),
    path("cambiarestado", views.cambiarEstado),
    path("registrarentrega", views.registrarentrega),
    path("categoriaplatos", views.categoriaplatos),
    path("platosprueba", views.obtenerCategoriasPorRestaurante),
    path("crearplato",views.registrar_plato,),
    path("nuevacategoria",views.crearCategoria),
    path("platospedidos",views.obtenerPlatosRegistradosPorRestaurante),
    path("ObtenerSoloPedido_filrado_codigo/listar",views.ObtenerSoloPedido_filrado_codigo)
]