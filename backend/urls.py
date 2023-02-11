from django.urls import path
from . import views
urlpatterns=[
    path("dish/listar",views.obtenerPlatos),
    path("loginrestaurante",views.restaurant_login)
]