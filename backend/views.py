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
from .models import Recomendacion
from django.db import models
# Create your views here.

@csrf_exempt
def obtener_restaurantes(request):
    if request.method == "GET":
        listaCategoriasQuerySet = Restaurante.objects.all()
        listaCategorias = []
        for c in listaCategoriasQuerySet:
            listaCategorias.append({
                "id": c.id,
                "nombre" : c.nombre,
                "email" : c.email,
                "password":c.password,
                "phone":c.telefono
            })

        dictOK = {
            "error" : "",
            "restaurantes" : listaCategorias
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
        categoria = request.GET.get("categoria")
        if int(categoria) == 0:
            restaurantesQueryset = Restaurante.objects.all().order_by('nombre')
        else:
            categorias = ["", "Cafeteria", "Food Trucks", "Platos", "Snacks", "Tiendas"]
            restaurantesQueryset = Restaurante.objects.filter(categoría__categoría=categorias[int(categoria)]).order_by('nombre')
        
        restaurantes = []
        for r in restaurantesQueryset:
            restaurantes.append({
                "nombre" : r.nombre,
                "categoria" : r.categoría.id,
                "estado" : int(r.estado),
                "imagen" : r.imagen
            })

        dictResponse = {
            "error" : "",
            "restaurantes" : restaurantes
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
    # recomendaciones = [
    #     {"id" : 1, "imagen" : "https://i.imgur.com/dVNYDI0.png", "texto" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
    #     {"id" : 2, "imagen" : "https://i.imgur.com/B4OGoqR.png", "texto" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
    #     {"id" : 3, "imagen" : "https://i.imgur.com/xYQlyoY.png", "texto" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
    #     {"id" : 4, "imagen" : "https://i.imgur.com/jxtsRAc.png", "texto" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
    # ]
    recomendacionesQuerySet = Recomendacion.objects.all()
    recomendaciones = []
    for r in recomendacionesQuerySet:
        recomendaciones.append({
            "imagen" : r.imagen,
            "texto" : r.texto
        })
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
    "Producto" : "Pizza",
    "Cantidad" : 3,
    "Precio" : 3.4,
    "Categoria_id" : 1,
    "Restaurante_id": 1,
    "Cliente_id": 1,
    "Codigo_verificación_id" : "53",
    "Estado":"1",
    "Registrado":"1"
    }
    """
@csrf_exempt
def ObtenerPedido_Registrar_7(request):
    #http://localhost:8000/backend/ObtenerPedido_Registrar_7/listar
    pedidos = []
    
    if request.method=="POST":
        #El Request esta siendo llamado.
        dictCode = json.loads(request.body)
        Producto = dictCode["Producto"]
        Cantidad = dictCode["Cantidad"]
        Precio = dictCode["Precio"]
        Categoria_id = dictCode["Categoria_id"]
        Restaurante_id = dictCode["Restaurante_id"]
        Cliente_id = dictCode["Cliente_id"]
        Codigo_verificación = dictCode["Codigo_verificación"]
        Estado = dictCode["Estado"]
        Registrado = dictCode["Registrado"]
        try:
            Categoria = CategoriaPlato.objects.get(id= Categoria_id)
        #En caso no se encuentre CategoriaPlato
        except CategoriaPlato.DoesNotExist:
            error = "La Categoria ingresada no se encuentra en la base de datos"
            dictError = {
               "error" : error
            }
            return HttpResponse(json.dumps(dictError))
        try:
            restaurantE = Restaurante.objects.get(id= Restaurante_id)
        #En caso no se encuentre CategoriaPlato
        except Restaurante.DoesNotExist:
            error = "El Restaurante ingresado no se encuentra en la base de datos"
            dictError = {
               "error" : error
            }
            return HttpResponse(json.dumps(dictError))
        try:
            Cliente = clienteulima.objects.get(id= Cliente_id)
        #En caso no se encuentre CategoriaPlato
        except clienteulima.DoesNotExist:
            error = "El Cliente ingresado no se encuentra en la base de datos"
            dictError = {
               "error" : error
            }
            return HttpResponse(json.dumps(dictError))
#HISOPO
        pedido = PlatoRegistrado(
            producto=Producto,
            cantidad=int(Cantidad),
            precio=float(Precio),
            categoría=Categoria,
            restaurante=restaurantE,
            cliente=Cliente,
            codigo_verificación=Codigo_verificación,
            estado=Estado,
            registrado=Registrado
        )
        pedido.save()

        if Estado=="1":
            rptaE="Confirmado"
        elif Estado=="2":
            rptaE="En preparación"
        else:
            rptaE="Entregado"
        

        if Registrado=="1":
            rptaR = "Si"
        else:
            rptaR="No"
        
        pedidos.append(
            {
        "Producto" : Producto,
        "Cantidad" : Cantidad,
        "Precio" : Precio,
        "Total" : float(Cantidad)*float(Precio),
        "Categoria" : Categoria.nombre,
        "Restaurante" : restaurantE.nombre,
        "Cliente" : Cliente.nombre,
        "Codigo_verificación" : Codigo_verificación,
        "Estado" : rptaE,
        "Registrado" : rptaR
        }
        )
        
        dictError = {
            "error" : "",
            "pedidos":pedidos
            
        }
        return HttpResponse(json.dumps(dictError))
    else:
        error = "Tipo de petición incorrecto, por favor usar POST"
        dictError = {
            "error" : error
        }
        return HttpResponse(json.dumps(dictError))
        

@csrf_exempt
def ObtenerSoloRestaurante_7(request):
    if request.method=="GET":
        #Lista en formato QuerySet
        #all() = saca todo el contenido
        ListaPedidosQuerySet = Restaurante.objects.all()
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
            ListaPedidos.append({
                      "id":c.id,
                      "nombre":c.nombre
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

@csrf_exempt
def ObtenerSoloCliente_7(request):
    if request.method=="GET":
        #Lista en formato QuerySet
        #all() = saca todo el contenido
        ListaPedidosQuerySet = clienteulima.objects.all()
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
            ListaPedidos.append({
                      "id":c.id,
                      "nombre":c.nombre
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

    # cuando quiere obtener los pedidos, llama un GET
    if request.method == "GET":
        pedidosQuerySet = PlatoRegistrado.objects.all().order_by('id')
        pedidos = []
        for p in pedidosQuerySet:
            pedidos.append({"id" : p.id, "detalles" : p.producto, "status" : int(p.estado)})
        dictResponse = {
            "error" : "",
            "arreglo" : pedidos
        }
        return HttpResponse(json.dumps(dictResponse))
    # cuando quiere modificar un pedido, llama un POST
    elif request.method == "POST":
        cuerpo = json.loads(request.body)
        identifier = cuerpo["id"]
        estado = cuerpo["estado"]
        PlatoRegistrado.objects.filter(pk=identifier).update(estado=estado)
        return HttpResponse("Se actualizo el pedido correctamente")
    else:
        return HttpResponse("Tipo de petición incorrecto")

@csrf_exempt
def registrarentrega(request):
    pedidos = []
    estados_imprimir = ["Confirmado", "En preparación", "Entregado"]
    if request.method == "POST":
        dictCode = json.loads(request.body)
        Codigo_verificación = dictCode["Codigo_verificación"]

        try:
            cat = PlatoRegistrado.objects.get(codigo_verificación=Codigo_verificación)
            if dictCode.get("estado") != None:
              cat.estado = dictCode.get("estado")
            #Codigo donde se registra la nuevo estado
            cat.save()
            filtrado = PlatoRegistrado.objects.filter(codigo_verificación=Codigo_verificación)
            for c in filtrado:#A esto se refiere con iterable
                pedidos.append({
                  "codigo_verificación":c.codigo_verificación,
                  "cliente":c.cliente.nombre,
                  "producto":c.producto,
                  "cantidad":c.cantidad,
                  "precio":c.precio,
                  "Total": c.precio*c.cantidad,
                  "estado":estados_imprimir[int(c.estado)-1]
                })
            dictOK = {
              "error" : "",
              "pedidos":pedidos
            }
            return HttpResponse(json.dumps(dictOK))
        
        except cat.DoesNotExist:
           dictError = {
               "error": "No se encontró ese pedido"
           }
           strError = json.dumps(dictError)
           return HttpResponse(json.dumps(strError))
        
    else:
        return HttpResponse("Tipo de petición incorrecto, por favor usar POST") 

@csrf_exempt
def ObtenerSoloPedido_filrado_codigo(request):
    if request.method=="GET":
        #Lista en formato QuerySet
        #all() = saca todo el contenido
        codigo = request.GET.get("codigo")
        ListaPedidos = []
        estados_imprimir = ["Confirmado", "En preparación", "Entregado"]

        if codigo == None:
            dictError = {
                "error": "Debe enviar una codigo como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)
        if codigo != "-1":   
           ListaPedidosQuerySet = PlatoRegistrado.objects.filter(codigo_verificación=codigo)
        
           for c in ListaPedidosQuerySet:
             ListaPedidos.append({
                  "codigo_verificación":c.codigo_verificación,
                  "cliente":c.cliente.nombre,
                  "producto":c.producto,
                  "cantidad":c.cantidad,
                  "precio":c.precio,
                  "Total": c.precio*c.cantidad,
                  "estado":estados_imprimir[int(c.estado)-1]
                })
        else:
            ListaPedidosQuerySet = PlatoRegistrado.objects.all()
        
            for c in ListaPedidosQuerySet:
              ListaPedidos.append({
                  "codigo_verificación":c.codigo_verificación,
                  "cliente":c.cliente.nombre,
                  "producto":c.producto,
                  "cantidad":c.cantidad,
                  "precio":c.precio,
                  "Total": c.precio*c.cantidad,
                  "estado":estados_imprimir[int(c.estado)-1]
                })

        dictOK = {
            "error" : "",
            "Pedidos" : ListaPedidos
        }
        return HttpResponse(json.dumps(dictOK))
        
    else:
        dictError = {
            "error": "Tipo de petición incorrecto, por favor usar GET"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    
        
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
