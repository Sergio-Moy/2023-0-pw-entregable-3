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
from .models import MostrarPlato
from django.db import models
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
        verofertasQuerySet = Oferta.objects.all()
        listadeofertas = []
        for v in verofertasQuerySet:
            listadeofertas.append({
                "id": v.id,
                "nombre" : v.nombre,
                "precio":v.precio,
                "imagen": v.imagen,
                "descripción": v.descripción,
                "categoria_id": v.categoría_id,
                "restaurante_id":v.restaurante_id,
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
                    "imagen":restaurante.imagen,
                    "id":restaurante.id
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
        if restaurante == None and categoria==None:
            dictError = {
                "error": "Debe enviar una categoria y restaurante como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        
        ListaPedidosQuerySet = MostrarPlato.objects.all()
        
        ListaPedidos = []
        
        
        #Convertir el tipo String a un int para q se conpare con el otro int=p["categoria"]
        if categoria=="-1":
          ListaPedidosQuerySet = MostrarPlato.objects.filter(restaurante__nombre=restaurante)
          for c in ListaPedidosQuerySet:
            ListaPedidos.append({
                      "id":c.id,
                      "producto":c.producto,
                      "precio":str(c.precio),
                      "restaurante": {
                        "nombre":c.restaurante.nombre
                      },
                      "categoria":{
                        "nombre":c.categoría.nombre
                      },
                      "imagen":c.imagen
                      
            })
        else:
            ListaPedidosQuerySet = MostrarPlato.objects.filter(categoría__nombre=categoria,restaurante__nombre=restaurante)
            for c in ListaPedidosQuerySet:
                
                ListaPedidos.append({
                      "id":c.id,
                      "producto":c.producto,
                      "precio":str(c.precio),
                      "restaurante": {
                        "nombre":c.restaurante.nombre
                      },
                      "categoria":{
                        "nombre":c.categoría.nombre
                      },
                      "imagen":c.imagen
                      
                })
        
        # TODO: Consultas a base de datos
        dictResponse = {
            "error": "",
            "platos_10": list(ListaPedidos)
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
        pedidosFiltradas = []
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
        restaurante = request.GET.get("restaurante")
        if restaurante == None:
            dictError = {
                "error": "Debe enviar una categoria y restaurante como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        
        ListaPedidosQuerySet = CategoriaPlato.objects.all()
        
        ListaPedidos = []
        
        
        #Convertir el tipo String a un int para q se conpare con el otro int=p["categoria"]
        if restaurante=="-1":
          for c in ListaPedidosQuerySet:
            ListaPedidos.append({
                      "id":c.id,
                      "nombre":c.nombre,
                      "restaurante": {
                        "nombre":c.restaurante.nombre
                      }
                      
            })
        else:
            ListaPedidosQuerySet = CategoriaPlato.objects.filter(restaurante__nombre=restaurante)
            for c in ListaPedidosQuerySet:
                ListaPedidos.append({
                      "id":c.id,
                      "nombre":c.nombre,
                      "restaurante": {
                        "nombre":c.restaurante.nombre
                      }
                      
                })
        
        # TODO: Consultas a base de datos
        dictResponse = {
            "error": "",
            "pedidos": list(ListaPedidos)
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
def ObtenerPedidos_8(request):
    if request.method=="GET":
        #Lista en formato QuerySet
        #all() = saca todo el contenido
        ListaPedidosQuerySet = PlatoRegistrado.objects.all()
        codigo = request.GET.get("codigo")
        ListaPedidos = []
        if codigo == None:
            dictError = {
                "error": "Debe enviar una codigo como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)   

        
        if codigo=="-1":
          for c in ListaPedidosQuerySet:
            print(c.cliente)
            ListaPedidos.append({
                      "id":c.id,
                      "producto":c.producto,
                      "codigo":c.codigo_verificación,
                      "precio":str(c.precio),
                      "cantidad":c.cantidad,
                      "restaurante": {
                        "nombre":c.restaurante.nombre
                      },
                      "categoria":{
                        "nombre":c.categoría.nombre
                      },
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
                      "restaurante": {
                        "nombre":c.restaurante.nombre
                      },
                      "categoria":{
                        "nombre":c.categoría.nombre
                      },
                      "estado":c.estado
                      
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

        if int(categoria) == 0:
            restaurantesFiltrados = restaurantes
        else:
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
"""
http://localhost:8000/backend/ObtenerPedido_Estado_14/listar
{
    "id" : 1,
    "estado" : "1"
}
"""
@csrf_exempt
def ObtenerPedido_Estado_14(request):
    if request.method=="POST":
        
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
        
        dicctCategoria = json.loads(request.body)
        identificador = dicctCategoria["id"]
        cat = PlatoRegistrado.objects.get(pk=identificador)
        if dicctCategoria.get("estado") != None:
           cat.estado = dicctCategoria.get("estado")
        cat.save()
        dictOK = {
           "error" : ""
        }
        return HttpResponse(json.dumps(dictOK))
        
    else:
        dictError = {
            "error" : "Tipo de petición incorrecto, usar GET"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
#http://localhost:8000/backend/ObtenerPedido_Registrar_7/listar
    """
    {
    "producto" : "Pizza",
    "cantidad" : 3,
    "precio" : 3.4,
    "categoría" : 1,
    "restaurante": 1,
    "cliente": 1,
    "codigo_verificación" : "53",
    "estado":"3",
    "registrado":"1"
    }
    """
@csrf_exempt
def ObtenerPedido_Registrar_7(request):

    #http://localhost:8000/backend/ObtenerPedido_Registrar_7/listar
    pedidos = []
    
    if request.method=="POST":
        #El Request esta siendo llamado.
        dictCode = json.loads(request.body)
        Nombre = dictCode["Nombre"]
        Producto = dictCode["Producto"]
        Direccion = dictCode["Direccion"]
        Cantidad = dictCode["Cantidad"]
        error = "No se encontró ese pedido"
        if Producto!=None and Nombre!=None and Direccion!=None and Cantidad!=None:
            pedidos.append(
                {
                    "Nombre":Nombre,
                    "Producto":Producto,
                    "Direccion":Direccion,
                    "Cantidad":Cantidad
                }
                )

            dictOK = {
                        "error": "",
                        "producto" : pedidos
            }
            strOK = json.dumps(dictOK)
            return HttpResponse(strOK)
        else:
            error = "Por favor envíe un Producto de pedido"
        dictError = {
            "error" : error
        }
        return HttpResponse(json.dumps(dictError))
    else:
        return HttpResponse("Tipo de petición incorrecto, por favor usar POST") 
    
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

    if request.method == "POST":
        cambios = []
        cuerpo = json.loads(request.body)
        for p in cuerpo:
            cambios.append(cuerpo[p])
        for i in range(4):
            if pedidos[i]["status"] < 2:
                pedidos[i]["status"] = pedidos[i]["status"] + cambios[i]
        dictResponse = {
            "error" : "",
            "arreglo" : pedidos
        }
        return HttpResponse(json.dumps(dictResponse))
    else:
        return HttpResponse("Tipo de petición incorrecto, por favor usar POST")

@csrf_exempt
def registrarentrega(request):
    pedidos = [
        {"code" : 123, "desc" : "Cheeseburger, Papas", "code_v" : 321},
        {"code" : 456, "desc" : "2x Cono Vainilla", "code_v" : 654},
        {"code" : 789, "desc" : "Cheese Fingers Familiar", "code_v" : 987},
    ]

    if request.method == "POST":
        dictCode = json.loads(request.body)
        code = dictCode["code"]
        error = "No se encontró ese pedido"
        if code != None:
            for pedido in pedidos:
                if int(code) == pedido["code"]:
                    dictOK = {
                        "error": "",
                        "producto" : pedido
                    }
                    strOK = json.dumps(dictOK)
                    return HttpResponse(strOK)
        else:
            error = "Por favor envíe un código de pedido"
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
@csrf_exempt       
def obtenerCategoriasPorRestaurante(request):
    if request.method == "GET":
        restaurante_id=request.GET.get("id")
        listaCategoriasQuerySet = CategoriaPlato.objects.filter(restaurante_id=restaurante_id)
        listaCategorias = []
        for c in listaCategoriasQuerySet:
            listaCategorias.append({
                "id" : c.id,
                "nombre" : c.nombre
            })

        dictOK = {
            "error" : "",
            "categorias" : listaCategorias
        }
        return HttpResponse(json.dumps(dictOK))

    else:
        dictError = {
            "error": "Tipo de petición no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

@csrf_exempt
def registrar_plato(request):
    if request.method != "POST":
        dictError = {
            "error": "Tipo de petición no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

    dictPlato = json.loads(request.body)
    nombre = dictPlato["producto"]
    categoria_id = dictPlato["categoria"]
    imagen = dictPlato["imagen"]
    precio = dictPlato["precio"]
    restaurante_id = dictPlato["restaurante"]

    # Obtener la categoria del plato
    try:
        categoria = CategoriaPlato.objects.get(id=categoria_id)
    except CategoriaPlato.DoesNotExist:
        dictError = {
            "error": "La categoría especificada no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

    # Obtener el restaurante
    try:
        restaurante = Restaurante.objects.get(id=restaurante_id)
    except Restaurante.DoesNotExist:
        dictError = {
            "error": "El restaurante especificado no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

    plato = MostrarPlato(
        restaurante=restaurante,
        categoría=categoria,
        producto=nombre,
        imagen=imagen,
        precio=precio
    )
    plato.save()

    dictOK = {
        "error": ""
    }
    return HttpResponse(json.dumps(dictOK))

@csrf_exempt
def crearCategoria(request):
    if request.method != "POST":
        dictError = {
            "error": "Tipo de petición no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

    dictCategoria = json.loads(request.body)
    restaurante_id = dictCategoria["restaurante"]
    nombre = dictCategoria["nombre"]

    try:
        restaurante = Restaurante.objects.get(id=restaurante_id)
    except Restaurante.DoesNotExist:
        dictError = {
            "error": "El restaurante no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError, status=404)

    categoria = CategoriaPlato(restaurante=restaurante, nombre=nombre)
    categoria.save()

    dictOK = {
        "error" : ""
    }
    return HttpResponse(json.dumps(dictOK))

@csrf_exempt
def obtenerPlatosRegistradosPorRestaurante(request):
    if request.method == "GET":
        restaurante_id = request.GET.get("id")
        platosQuerySet = PlatoRegistrado.objects.filter(restaurante_id=restaurante_id)
        platos = []
        for p in platosQuerySet:
            platos.append({
                "id": p.id,
                "producto": p.producto,
                "cantidad": p.cantidad,
                "precio": p.precio,
                "categoria_id": p.categoría.id,
                "categoria_nombre": p.categoría.nombre,
                "restaurante_id": p.restaurante.id,
                "restaurante_nombre": p.restaurante.nombre,
                "cliente_id": p.cliente.id,
                "cliente_nombre": p.cliente.nombre,
                "codigo_verificacion": p.codigo_verificación,
                "estado": p.estado,
                "registrado": p.registrado,
            })

        dictOK = {
            "error": "",
            "platos": platos
        }
        return HttpResponse(json.dumps(dictOK))
    else:
        dictError = {
            "error": "Tipo de petición no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
