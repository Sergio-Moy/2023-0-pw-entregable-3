from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Dish
from .serializers import DishSerializer
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant=request.user.restaurant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def obtenerPlatos(request):
    if request.method == "GET":
        categoria = request.GET.get("categoria")
        restaurante = request.GET.get("restaurante")

        if categoria == None or restaurante == None:
            dictError = {
                "error": "Debe enviar una categoria y restaurante como query parameters."
            }
            return JsonResponse(dictError)

        platos = Dish.objects.filter(category=categoria, restaurant=restaurante)

        dictResponse = {
            "error": "",
            "platos": list(platos)
        }
        return JsonResponse(dictResponse)
    else:
        dictError = {
            "error": "Tipo de petición no existe"
        }
        return JsonResponse(dictError)
