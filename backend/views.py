from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Restaurant
from .models import Dish

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.




def obtenerPlatos(request):
    if request.method == "GET":
        categoria = request.GET.get("categoria")

        if categoria == None:
            dictError = {
                "error": "Debe enviar una categoria como query paremeter."
            }
            strError = json.dumps(dictError)
            return HttpResponse(strError)

        peliculas = [
            {
                "id": 1,
                "nombre": "Avatar 2",
                "url": "https://i.blogs.es/6b43d1/avatar-edicion-especial-cartel/450_1000.jpg",
                "categoria": 1
            }, {
                "id": 2,
                "nombre": "El gato con botas",
                "url": "https://www.universalpictures-latam.com/tl_files/content/movies/puss_in_boots_2/posters/01.jpg",
                "categoria": 2
            }, {
                "id": 3,
                "nombre": "Transformer, el despertar de las bestias",
                "url": "https://es.web.img3.acsta.net/pictures/22/12/02/09/33/5399733.jpg",
                "categoria": 3
            }
        ]

        peliculasFiltradas = []
        if categoria == "-1":
            # No se debe filtrar nana
            peliculasFiltradas = peliculas
        else :
            for p in peliculas:
                if p["categoria"] == int(categoria):
                    peliculasFiltradas.append(p)
        
        # TODO: Consultas a bd
        dictResponse = {
            "error": "",
            "peliculas": list(peliculasFiltradas)
        }
        strResponse = json.dumps(dictResponse)
        return HttpResponse(strResponse)
    else:
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

def restaurant_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        restaurant = authenticate(email=email, password=password)
        if restaurant is not None:
            login(request, restaurant)
            return redirect("home")
        else:
            return render(request, "login.html", {"error_message": "Invalid login"})
    else:
        return render(request, "login.html")

@login_required(login_url="login")
def home(request):
    return render(request, "home.html")