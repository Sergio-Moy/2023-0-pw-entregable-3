from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Restaurant
from .models import Dish
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from . models import Categorias
from django.http import JsonResponse
from .models import Restaurant
from . models import Pedidos
# Create your views here.

@csrf_exempt
def obtener_restaurantes(request):
    if request.method == "GET":
        listaCategoriasQuerySet = Restaurant.objects.all()
        listaCategorias = []
        for c in listaCategoriasQuerySet:
            listaCategorias.append({
                "name" : c.name,
                "email" : c.email,
                "password":c.password,
                "address":c.address,
                "phone":c.phone
            })

        dictOK = {
            "error" : "",
            "categorias" : listaCategorias
        }
        return HttpResponse(json.dumps(dictOK))

    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

@csrf_exempt
def loginRestaurante(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["email"]
        password = dictDataRequest["password"]

        restaurante = Restaurant.objects.filter(email=usuario, password=password).first()
        if restaurante:
            dictOK = {
                "error": "",
                "restaurante": {
                    "id": restaurante.id,
                    "email": restaurante.email,
                }
            }
            return HttpResponse(json.dumps(dictOK))
        else:
            dictError = {
                "error": "Credenciales incorrectas"
            }
            strError = json.dumps(usuario)
            return HttpResponse(strError)
    else:
        dictError = {
            "error": "Tipo de petición no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

@csrf_exempt
def obtenerPlatos_10(request):
    if request.method == "GET":
        #http://127.0.0.1:8000/backend/platos_10/listar?categoria=-1&restaurante=-1
        categoria = request.GET.get("categoria")
        restaurante = request.GET.get("restaurante")
        if categoria == None and restaurante == None:
            dictError = {
                "error": "Debe enviar una categoria y restaurante como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        platos_10 = [
            {
                "id": 1,
                "Restaurante": 1,
                "Categoria": 1,
                "Producto" : "Limonada Frozen (1.5L)",
                "Precio": 18.5,
                "Imagen":"https://www.ahorrarnuncafuetanbueno.com.pe/wp-content/uploads/2022/02/Limonada_frozen_912x700.jpg",
                "Izq": "#3",
                "Der": "#2"
            }, {
                "id": 2,
                "Restaurante": 1,
                "Categoria": 1,
                "Producto" : "Cusqueña (310 ml)",
                "Precio": 4.5,
                "Imagen":"https://polleriaslagranja.com/wp-content/uploads/2022/10/La-Granja-Real-Food-Chicken-Cusquena.png",
                "Izq": "#1",
                "Der": "#3"
            }, {
                "id": 3,
                "Restaurante": 1,
                "Categoria": 1,
                "Producto" : "Inca Cola (1.5L)",
                "Precio": 6.5,
                "Imagen":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-73bW05hAU7jQDiqAgHB70rh2TGOYSW8Gvw&usqp=CAU",
                "Izq": "#2",
                "Der": "#1"
            }, {
                "id" : 4,
                "Restaurante": 1,
                "Categoria": 2,
                "Producto" : "Ceviche Familiar",
                "Precio": 19.50,
                "Imagen":"https://micevichedehoy.com/wp-content/uploads/2018/12/ceviche-de-pescado_700x465-700x465.jpg",
                "Izq": "#6",
                "Der": "#5"
            }, {
                "id" : 5,
                "Restaurante": 1,
                "Categoria": 2,
                "Producto" : "Sopa de cangrejo",
                "Precio": 16.00,
                "Imagen":"https://recetas.7maravillasgastronomicas.com/wp-content/uploads/2011/01/concentradodecangrejo.jpg",
                "Izq": "#4",
                "Der": "#6"
            }, {
                "id" : 6,
                "Restaurante": 1,
                "Categoria": 2,
                "Producto" : "Pescado con lenteja (Yuca y ensalada)",
                "Precio": 22.50,
                "Imagen":"https://3.bp.blogspot.com/-u-yN3kRr03o/Wy1cxQU5wWI/AAAAAAAAL7I/5VlvYZ6Iev8eGYUHZ2LvUbG7XcAZp-1zQCLcBGAs/s1600/Guiso%2Bde%2BLentejas%2Bcon%2BPescado%2BFrito.jpg",
                "Izq": "#5",
                "Der": "#4"
            }, {
                "id" : 7,
                "Restaurante": 2,
                "Categoria": 3,
                "Producto" : "Bisteck a lo pobre (papas, ensalada, arroz, platano y huevo)",
                "Precio": 28.50,
                "Imagen":"https://iperu.pe/wp-content/uploads/2019/08/bistec-a-lo-pobre_800x534.jpg",
                "Izq": "#9",
                "Der": "#8"
            }, {
                "id" : 8,
                "Restaurante": 2,
                "Categoria": 3,
                "Producto" : "Bisteck (papas, ensalada y arroz)",
                "Precio": 27.50,
                "Imagen":"https://1.bp.blogspot.com/-4THw7fRcvBs/Wl6V87BAf2I/AAAAAAAAAEk/Tqh1sOnKZPANDwOO3-zyfGO-ImgU4lBBQCLcBGAs/s1600/Bistek%2Ba%2Bla%2BParrilla.jpg",
                "Izq": "#7",
                "Der": "#9"
            }, {
                "id" : 9,
                "Restaurante": 2,
                "Categoria": 3,
                "Producto" : "Lomo salatado",
                "Precio": 19.00,
                "Imagen":"https://decomidaperuana.com/wp-content/uploads/2020/10/lomo-saltado.jpg",
                "Izq": "#8",
                "Der": "#7"
            }
        ]

        platos_10Filtradas = []
        #Convertir el tipo String a un int para q se conpare con el otro int=p["categoria"]
        if categoria == "-1" and restaurante=="-1":
            #no se va a filtrar
            platos_10Filtradas = platos_10
        else:
            for p in platos_10:
               if p["Categoria"] == int(categoria) and p["Restaurante"] == int(restaurante):
                  platos_10Filtradas.append(p)
        
        # TODO: Consultas a base de datos
        dictResponse = {
            "error": "",
            "platos_10": list(platos_10Filtradas)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)


def ObtenerCategorias_10(request):
    if request.method=="GET":
        #Lista en formato QuerySet
        #Filtrar categorias cuyo estado sea A de Activo
        ListaCategoriasQuerySet = Categorias.objects.filter(estado=1)
        #Restaurante
        restaurante = request.GET.get("restaurante")
    #ListaCategorias = list(ListaCategoriasQuerySet)#convertido a lista de python (NO FUNCIONA)
        #En su reemplazo hacemos esto:
        ListaCategorias = []
        if restaurante=="-1":
         for c in ListaCategoriasQuerySet:
            ListaCategorias.append({
                "id":c.id,
                "nombre":c.name,
                "restaurante":c.restaurantes
            })#convertido a lista de python
        else:
            ListaCategoriasQuerySet = Categorias.objects.filter(restaurantes=int(restaurante))
            for c in ListaCategoriasQuerySet:
                ListaCategorias.append({
                      "id":c.id,
                      "nombre":c.name,
                      "restaurante":c.restaurantes
                })#convertido a lista de python

        dictOK = {
            "error" : "",
            "categoria" : ListaCategorias
        }
        #Para retornarlo en el frondend, tengo que convertirlo a un String JSON y no dicc
        return HttpResponse(json.dumps(dictOK))
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

def ObtenerPedidos_8(request):
    if request.method=="GET":
        #Lista en formato QuerySet
        #all() = saca todo el contenido
        ListaPedidosQuerySet = Pedidos.objects.all()
        codigo = request.GET.get("codigo")
        ListaPedidos = []
        if codigo=="-1":
          for c in ListaPedidosQuerySet:
            ListaPedidos.append({
                "id":c.id,
                "producto":c.producto,
                "codigo":c.codigo,
                "precio":str(c.precio),
                "cantidad":c.cantidad,
                "restaurante": c.restaurantes
            })
        else:
            ListaPedidosQuerySet = Pedidos.objects.filter(codigo=int(codigo))
            for c in ListaPedidosQuerySet:
                ListaPedidos.append({
                      "id":c.id,
                      "producto":c.producto,
                      "codigo":c.codigo,
                      "precio":str(c.precio),
                      "cantidad":c.cantidad,
                      "restaurante": c.restaurantes
                })

        dictOK = {
            "error" : "",
            "Pedidos" : ListaPedidos
        }
        return HttpResponse(json.dumps(dictOK))
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)