from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
from .models import Restaurante
from .models import clienteulima
from .models import Oferta
from .models import PlatoRegistrado
from .models import CategoriaPlato
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
def obtener_ofertas(request):
    if request.method == "GET":
        verofertasQuerySet = ofertas.objects.all()
        listadeofertas = []
        for v in verofertasQuerySet:
            listadeofertas.append({
                "nombre" : v.name,
                "codigo" : v.codigo,
                "precio":v.password,
                "restaurante":v.restaurante,
            })

        dictOK = {
            "error" : "",
            "ofertas" : listadeofertas
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
        restaurante = Restaurante.objects.filter(email=usuario, password=password).first()
        if restaurante:
            dictOK = {
                "error": "",
                "restaurante": {
                    "nombre": restaurante.nombre,
                    "telefono": restaurante.telefono,
                    "imagen":restaurante.imagen
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

@csrf_exempt
def ObtenerCategorias_10(request):
    if request.method=="GET":
        restaurante = request.GET.get("restaurante")
        if restaurante == None:
            dictError = {
                "error": "Debe enviar una categoria y restaurante como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        pedidos = [
            {
                "id": 1,
                "Restaurante": "Punto y Sabor",
                "Categoria": "Bebidas",
                "Producto" : "Limonada Frozen (1.5L)",
                "Cantidad" : 3,
                "Precio": 18.5,
                "Cliente": 2020,
                "Codigo_verificacion" : 51,
                "Estado" : "Preparacion",
                "Registrado" : "Si"
            }, {
                "id": 2,
                "Restaurante": "Punto y Sabor",
                "Categoria": "Bebidas",
                "Producto" : "Cusqueña (310 ml)",
                "Cantidad" : 2,
                "Precio": 4.5,
                "Cliente": 2020,
                "Codigo_verificacion" : 52,
                "Estado" : "Preparacion",
                "Registrado" : "Si"
            }, {
                "id": 3,
                "Restaurante": "Corralito",
                "Categoria": "Bebidas",
                "Producto" : "Inca Cola (1.5L)",
                "Cantidad" : 2,
                "Precio": 6.5,
                "Cliente": 1166,
                "Codigo_verificacion" : 53,
                "Estado" : "Confirmacion",
                "Registrado" : "Si"
            },
            {
                "id" : 4,
                "Restaurante": "Corralito",
                "Categoria": "Carnes",
                "Producto" : "Bisteck (papas, ensalada y arroz)",
                "Cantidad" : 1,
                "Precio": 27.50,
                "Cliente": 1166,
                "Codigo_verificacion" : 54,
                "Estado" : "Confirmacion",
                "Registrado" : "Si"
            }
        ]

        pedidosFiltradas = []
        #Convertir el tipo String a un int para q se conpare con el otro int=p["categoria"]
        if restaurante=="-1":
            #no se va a filtrar
            pedidosFiltradas = pedidos
        else:
            for p in pedidos:
               if p["Restaurante"] == restaurante:
                  pedidosFiltradas.append(p)
        
        # TODO: Consultas a base de datos
        dictResponse = {
            "error": "",
            "pedidos": list(pedidosFiltradas)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
        """
                        #HOLALAAALA
        restaurante = request.GET.get("restaurante")        
        ListaCategoria = PlatoRegistrado.objects.all()
        ListaFiltrada = []
        if restaurante == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

        if restaurante=="-1":
            for c in ListaCategoria:
                ListaFiltrada.append({
                   "id":c.id,
                   "nombre":c.producto,
                   "categoría":c.categoría
                })#convertido a lista de python
        else:
            for c in ListaCategoria:
                if restaurante == c.restaurante:
                    ListaFiltrada.append({
                       "id":c.id,
                       "nombre":c.producto,
                       "categoría":c.categoría
                   })#convertido a lista de python

        dictOK = {
            "error" : "",
            "categoria" : ListaFiltrada
        }
        #Para retornarlo en el frondend, tengo que convertirlo a un String JSON y no dicc
        return HttpResponse(json.dumps(dictOK))
        """
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
@csrf_exempt
def ObtenerPedidos_8(request):
    if request.method=="GET":
        cliente = request.GET.get("codigo")
        if cliente == None:
            dictError = {
                "error": "Debe enviar una categoria y restaurante como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        pedidos = [
            {
                "id": 1,
                "Restaurante": "Punto y Sabor",
                "Categoria": "Bebidas",
                "Producto" : "Limonada Frozen (1.5L)",
                "Cantidad" : 3,
                "Precio": 18.5,
                "Cliente": 2020,
                "Codigo_verificacion" : 51,
                "Estado" : "Preparacion",
                "Registrado" : "Si"
            }, {
                "id": 2,
                "Restaurante": "Punto y Sabor",
                "Categoria": "Bebidas",
                "Producto" : "Cusqueña (310 ml)",
                "Cantidad" : 2,
                "Precio": 4.5,
                "Cliente": 2020,
                "Codigo_verificacion" : 52,
                "Estado" : "Preparacion",
                "Registrado" : "Si"
            }, {
                "id": 3,
                "Restaurante": "Corralito",
                "Categoria": "Bebidas",
                "Producto" : "Inca Cola (1.5L)",
                "Cantidad" : 2,
                "Precio": 6.5,
                "Cliente": 1166,
                "Codigo_verificacion" : 53,
                "Estado" : "Confirmacion",
                "Registrado" : "Si"
            },
            {
                "id" : 4,
                "Restaurante": "Corralito",
                "Categoria": "Carnes",
                "Producto" : "Bisteck (papas, ensalada y arroz)",
                "Cantidad" : 1,
                "Precio": 27.50,
                "Cliente": 1166,
                "Codigo_verificacion" : 54,
                "Estado" : "Confirmacion",
                "Registrado" : "Si"
            }
        ]

        pedidosFiltradas = []
        #Convertir el tipo String a un int para q se conpare con el otro int=p["categoria"]
        if cliente=="-1":
            #no se va a filtrar
            pedidosFiltradas = pedidos
        else:
            for p in pedidos:
               if p["Cliente"] == int(cliente):
                  pedidosFiltradas.append(p)
        
        # TODO: Consultas a base de datos
        dictResponse = {
            "error": "",
            "pedidos": list(pedidosFiltradas)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
        """
        #Lista en formato QuerySet
        #all() = saca todo el contenido
        ListaPedidosQuerySet = PlatoRegistrado.objects.all()
        codigo = request.GET.get("codigo")
        ListaPedidos = []
        if codigo=="-1":
          for c in ListaPedidosQuerySet:
            ListaPedidos.append({
                      "id":c.id,
                      "producto":c.producto,
                      "codigo":c.codigo_verificación,
                      "precio":str(c.precio),
                      "cantidad":c.cantidad,
                      "estado":c.categoría,
                      "restaurante": c.restaurante,
                      "cliente": c.cliente,
                      "estado":c.estado
            })
        else:
            ListaPedidosQuerySet = PlatoRegistrado.objects.filter(codigo_verificación=int(codigo))
            for c in ListaPedidosQuerySet:
                ListaPedidos.append({
                      "id":c.id,
                      "producto":c.producto,
                      "codigo":c.codigo_verificación,
                      "precio":str(c.precio),
                      "cantidad":c.cantidad,
                      "estado":c.categoría,
                      "restaurante": c.restaurante,
                      "cliente": c.cliente,
                      "estado":c.estado
                })

        dictOK = {
            "error" : "",
            "Pedidos" : ListaPedidos
        }
        return HttpResponse(json.dumps(dictOK))
        """
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

def ObtenerListado(request):
    if request.method == "GET":
        restaurantes = [
            {"id": 1, "nombre": "Cafeteria F", "categoria" : 1, "estado" : 1, "imagen" : "https://i.imgur.com/PoeLtRF.png"},
            {"id": 2, "nombre": "Cafeteria O", "categoria" : 1, "estado" : 1, "imagen" : "https://i.imgur.com/PoeLtRF.png"},
            {"id": 3, "nombre": "Cayetana", "categoria" : 2, "estado" : 1, "imagen" : "https://i.imgur.com/Gj3oj0r.png"},
            {"id": 4, "nombre": "Capirotes", "categoria" : 2, "estado" : 1, "imagen" : "https://i.imgur.com/Gj3oj0r.png"},
            {"id": 5, "nombre": "Bembos", "categoria" : 3, "estado" : 1, "imagen" : "https://i.imgur.com/wRAODhP.png"},
            {"id": 6, "nombre": "Chifa Express", "categoria" : 3, "estado" : 0, "imagen" : "https://i.imgur.com/FlCQAxe.png"},
            {"id": 7, "nombre": "Mr. Sushi", "categoria" : 3, "estado" : 0, "imagen" : "https://i.imgur.com/XBz0LyW.png"},
            {"id": 8, "nombre": "Nevera Fit", "categoria" : 3, "estado" : 1, "imagen" : "https://i.imgur.com/4LKr8Hm.png"},
            {"id": 9, "nombre": "Dunkin' Donuts", "categoria" : 4, "estado" : 1, "imagen" : "https://i.imgur.com/gE20Djg.png"},
            {"id": 10, "nombre": "GoGreen", "categoria" : 4, "estado" : 1, "imagen" : "https://i.imgur.com/rbPjXK5.png"},
            {"id": 11, "nombre": "Momenti", "categoria" : 4, "estado" : 1, "imagen" : "https://i.imgur.com/vYgSE5e.png"},
            {"id": 12, "nombre": "Starbucks", "categoria" : 4, "estado" : 0, "imagen" : "https://i.imgur.com/bzLj6kE.png"},
            {"id": 13, "nombre": "Listo", "categoria" : 5, "estado" : 1, "imagen" : "https://i.imgur.com/rAV8SfV.png"},
            {"id": 14, "nombre": "Quiosco D", "categoria" : 5, "estado" : 0, "imagen" : "https://i.imgur.com/afudJgV.png"},
            {"id": 15, "nombre": "Quiosco N", "categoria" : 5, "estado" : 1, "imagen" : "https://i.imgur.com/afudJgV.png"},
            ]

        categoria = request.GET.get("categoria")
        restaurantesFiltrados = []

        for r in restaurantes:
            if r["categoria"] == int(categoria):
                restaurantesFiltrados.append(r)
        dictResponse = {
            "error" : "",
            "restaurantes" : restaurantesFiltrados
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)

    else:
        dictError = {
            "error" : "Tipo de petición incorrecto, usar GET"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError) 

def ObtenerRecomendaciones(request):
    recomendaciones = [
        {"id" : 1, "imagen" : "https://i.imgur.com/dVNYDI0.png", "texto" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
        {"id" : 2, "imagen" : "https://i.imgur.com/B4OGoqR.png", "texto" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
        {"id" : 3, "imagen" : "https://i.imgur.com/xYQlyoY.png", "texto" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
        {"id" : 4, "imagen" : "https://i.imgur.com/jxtsRAc.png", "texto" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
    ]
    dictResponse = {
        "error" : "",
        "recomendaciones" : recomendaciones
    }
    strResponse = json.dumps(dictResponse)
    return HttpResponse(strResponse)

@csrf_exempt
def loginCliente(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["Codigo"]
        password = dictDataRequest["password"]

        Cliente = clienteulima.objects.filter(codigo =usuario, password=password).first()
        if Cliente:
            dictOK = {
                "error": "",
                "Cliente": {
                    "codigo": Cliente.codigo,
                    "nombre": Cliente.nombre
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
def ObtenerPedido_Estado_14(request):
    if request.method=="GET":
        estado = request.GET.get("estado")
        codigo = request.GET.get("codigo")
        if estado == None and codigo ==None:
            dictError = {
                "error": "Debe enviar una categoria y restaurante como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        pedidos = [
            {
                "id": 1,
                "Restaurante": "Punto y Sabor",
                "Categoria": "Bebidas",
                "Producto" : "Limonada Frozen (1.5L)",
                "Cantidad" : 3,
                "Precio": 18.5,
                "Cliente": 2020,
                "Codigo_verificacion" : 51,
                "Estado" : "Preparacion",
                "Registrado" : "Si"
            }, {
                "id": 2,
                "Restaurante": "Punto y Sabor",
                "Categoria": "Bebidas",
                "Producto" : "Cusqueña (310 ml)",
                "Cantidad" : 2,
                "Precio": 4.5,
                "Cliente": 2020,
                "Codigo_verificacion" : 52,
                "Estado" : "Preparacion",
                "Registrado" : "Si"
            }, {
                "id": 3,
                "Restaurante": "Corralito",
                "Categoria": "Bebidas",
                "Producto" : "Inca Cola (1.5L)",
                "Cantidad" : 2,
                "Precio": 6.5,
                "Cliente": 1166,
                "Codigo_verificacion" : 53,
                "Estado" : "Confirmacion",
                "Registrado" : "Si"
            },
            {
                "id" : 4,
                "Restaurante": "Corralito",
                "Categoria": "Carnes",
                "Producto" : "Bisteck (papas, ensalada y arroz)",
                "Cantidad" : 1,
                "Precio": 27.50,
                "Cliente": 1166,
                "Codigo_verificacion" : 54,
                "Estado" : "Confirmacion",
                "Registrado" : "Si"
            }
        ]

        pedidosFiltradas = []
        #Convertir el tipo String a un int para q se conpare con el otro int=p["categoria"]
        for c in pedidos:
            if int(codigo )== c["Codigo_verificacion"]:
                c["Estado"] = estado
        pedidosFiltradas = pedidos

        # TODO: Consultas a base de datos
        dictResponse = {
            "error": "",
            "pedidos": list(pedidosFiltradas)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
        """
        ListaPedidosQuerySet = PlatoRegistrado.objects.all()
        estado = request.GET.get("estado")
        codigo = request.GET.get("codigo")
        ListaPedidos = []

        for c in ListaPedidosQuerySet:
            if int(codigo )== c.codigo_verificación:
                c.codigo_verificación = int(estado)

        for c in ListaPedidosQuerySet:
            ListaPedidos.append({
                      "id":c.id,
                      "producto":c.producto,
                      "codigo":c.codigo_verificación,
                      "precio":str(c.precio),
                      "cantidad":c.cantidad,
                      "estado":c.categoría,
                      "restaurante": c.restaurante,
                      "cliente": c.cliente,
                      "estado":c.estado
            })

        dictOK = {
            "error" : "",
            "Pedidos" : ListaPedidos
        }
        return HttpResponse(json.dumps(dictOK))
        """
    else:
        dictError = {
            "error" : "Tipo de petición incorrecto, usar GET"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
@csrf_exempt
def ObtenerPedido_Registrar_7(request):
    #http://localhost:8000/backend/ObtenerPedido_Registrar_7/listar?codigo=30&direccion=Distrito%2013%20%20jr%20Bolivar
    #Nota: el espacio se hace con %20
    
    if request.method=="GET":
        direccion = request.GET.get("direccion")
        codigo = request.GET.get("codigo")
        if direccion == None and codigo ==None:
            dictError = {
                "error": "Debe enviar una categoria y restaurante como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        pedidos = [
            {
                "id": 1,
                "Restaurante": "Punto y Sabor",
                "Categoria": "Bebidas",
                "Producto" : "Limonada Frozen (1.5L)",
                "Cantidad" : 3,
                "Precio": 18.5,
                "Cliente": 2020,
                "Codigo_verificacion" : 51,
                "Estado" : "Preparacion",
                "Registrado" : "Si"
            }, {
                "id": 2,
                "Restaurante": "Punto y Sabor",
                "Categoria": "Bebidas",
                "Producto" : "Cusqueña (310 ml)",
                "Cantidad" : 2,
                "Precio": 4.5,
                "Cliente": 2020,
                "Codigo_verificacion" : 52,
                "Estado" : "Preparacion",
                "Registrado" : "Si"
            }, {
                "id": 3,
                "Restaurante": "Corralito",
                "Categoria": "Bebidas",
                "Producto" : "Inca Cola (1.5L)",
                "Cantidad" : 2,
                "Precio": 6.5,
                "Cliente": 1166,
                "Codigo_verificacion" : 53,
                "Estado" : "Confirmacion",
                "Registrado" : "Si"
            },
            {
                "id" : 4,
                "Restaurante": "Corralito",
                "Categoria": "Carnes",
                "Producto" : "Bisteck (papas, ensalada y arroz)",
                "Cantidad" : 1,
                "Precio": 27.50,
                "Cliente": 1166,
                "Codigo_verificacion" : 54,
                "Estado" : "Confirmacion",
                "Registrado" : "Si"
            }
        ]

        pedidosFiltradas = []
        #Convertir el tipo String a un int para q se conpare con el otro int=p["categoria"]
        pedidosFiltradas = pedidos
        pedidosFiltradas.append(
            {
                "Cliente":codigo,
                "Direccion": direccion
            }
        )

        # TODO: Consultas a base de datos
        dictResponse = {
            "error": "",
            "pedidos": list(pedidosFiltradas)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de petición no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    """
        ListaPedidosQuerySet = Pedidos.objects.all()
        codigo = request.GET.get("codigo")
        direccion = request.GET.get("direccion")
        ListaPedidos = []

        for c in ListaPedidosQuerySet:
            ListaPedidos.append({
                      "id":c.id,
                      "producto":c.producto,
                      "codigo":c.codigo_verificación,
                      "precio":str(c.precio),
                      "cantidad":c.cantidad,
                      "estado":c.categoría,
                      "restaurante": c.restaurante,
                      "cliente": c.cliente,
                      "estado":c.estado
            })
        ListaPedidos.append({
            "codigo":codigo,
            "direccion": direccion
        })

        dictOK = {
            "error" : "",
            "Pedidos" : ListaPedidos
        }
        return HttpResponse(json.dumps(dictOK))
    """
    

@csrf_exempt
def register_plato(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        imagen = request.POST.get('imagen')
        restaurante = request.user.restaurante
        categoria = request.POST.get('categoria')

        plato = Plato.objects.create(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            imagen=imagen,
            restaurante=restaurante,
            categoria=categoria
        )

        return redirect('plato_details', plato_id=plato.id)

    return render(request, 'register_plato.html')

@csrf_exempt
def show_orders(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    orders = PlatoRegistrado.objects.filter(restaurant=restaurant)
    return render(request, 'orders.html', {'orders': orders})

@csrf_exempt
def register_categoria(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')

        categoria = CategoriaPlato.objects.create(
            nombre=categoria
        )

        return redirect('plato_details', plato_id=categoria.id)

    return render(request, 'register_plato.html')

@csrf_exempt
def cambiarEstado(request):
    pedidos = [
        {"id" : 1, "detalles" : "Cheeseburger Regular", "status" : 0},
        {"id" : 2, "detalles" : "Papas Regulares", "status" : 1},
        {"id" : 3, "detalles" : "Bebida Mediana", "status" : 2},
        {"id" : 4, "detalles" : "Cono Vainilla", "status" : 1},
    ]

    if request.method == "GET":
        dictResponse = {
            "error" : "",
            "arreglo" : pedidos
        }
        return HttpResponse(json.dumps(dictResponse))
    else:
        return HttpResponse("Tipo de petición incorrecto, por favor usar GET")

@csrf_exempt
def registrarentrega(request):
    pedidos = [
        {"code" : 123, "desc" : "Cheeseburger, Papas", "code_v" : 321},
        {"code" : 456, "desc" : "2x Cono Vainilla", "code_v" : 654},
        {"code" : 789, "desc" : "Cheese Fingers Familiar", "code_v" : 987},
    ]

    if request.method == "POST":
        req = json.loads(request.body)
        code = req["code"]
        codev = req["code_v"]
        error = "No se encontró un pedido con ese código"
        for i in pedidos:
            if code == i["code"]:
                if codev == i["code_v"]:
                    dictOk = {
                        "error" : "",
                        "mensaje" : "Código de verificación correcto, entrega registrada"
                    }
                    strOk = json.dumps(dictOk)
                    return HttpResponse(strOk)
                else:
                    error = "El código de verificación es incorrecto"
        dictError = {
            "error" : error
        }
        return HttpResponse(json.dumps(dictError))
    else:
        return HttpResponse("Tipo de petición incorrecto, por favor usar POST")
    
        
@csrf_exempt
def categoriaplatos(request):
    if request.method == "GET": 
        restaurante = request.GET.get("restaurante")
        categoria = request.GET.get("categoria")
        if restaurante == None and categoria == None: 
            dictError = {
                "error": "Debe enviar una categoria y restaurante como query parameter. "
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        platos = [
            {
               "id": 1,
                "Restaurante": "bembos",
                "Categoria": "Bebidas",
                "Producto" : "Gaseosa Inkacola",
                "Precio": 18.5
            },{
                "id": 2,
                "Restaurante": "Bembos",
                "Categoria": "hamburguesas",
                "Producto" : "Hamburguesa de parrilla",
                "Precio": 19.5
            },{
                "id": 3,
                "Restaurante": "Bembos",
                "Categoria": "Complementos",
                "Producto" : "Porción de papitas grande",
                "Precio": 9.5
            },{
                "id": 4,
                "Restaurante": "Bembos",
                "Categoria": "Helados",
                "Producto" : "Helado de vainilla grande",
                "Precio": 3.5
            },{
                "id": 5,
                "Restaurante": "Cafeteria O",
                "Categoria": "Combos",
                "Producto" : " 6 porciones de pollo + 1 porción de papitas",
                "Precio": 23.5
            },{
                "id": 6,
                "Restaurante": "Cafeteria O",
                "Categoria": "Nugets",
                "Producto" : "24 Nugets + 1 porcíon de papitas grande",
                "Precio": 20.5
            },{
                "id": 7,
                "Restaurante": "Cafeteria O",
                "Categoria": "Almuerzos",
                "Producto" : "Ají de gallina",
                "Precio": 12.5
            },{
                "id": 8,
                "Restaurante": "Cafeteria O",
                "Categoria": "Desayuno",
                "Producto" : "Café + Pan con Pollo",
                "Precio": 5.5
            }, {
                "id": 9,
                "Restaurante": "Cafeteria O",
                "Categoria": "Cena",
                "Producto" : "Salchipapa",
                "Precio": 12.5
            }
        ]
        categoriaplatos = []
        #Convertir el tipo String a un int para q se conpare con el otro int=p["categoria"]
        if restaurante=="-1":
            #no se va a filtrar
            categoriaplatos = platos
        else:
            for n in platos:
               if n["Restaurante"] == restaurante:
                  categoriaplatos.append(n)
        
        # TODO: Consultas a base de datos
        dictResponse = {
            "error": "",
            "platos": list(categoriaplatos)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
        

    
    