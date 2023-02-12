from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.CharField(max_length=30)

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class Categorias(models.Model):
    
    RESTAURANTES_CATEGORIA = (
        (1,"Sabor y punto"),
        (2,"Corralito"),
        (3,"Sabores y mixturas")
    )

    ESTADO_CATEGORIA = (
        (1,"Activo"),
        (2,"Inactivo")
    )

    name = models.CharField(max_length=255)
    estado = models.IntegerField(max_length=1, choices=ESTADO_CATEGORIA)
    restaurantes = models.IntegerField(max_length=1, choices=RESTAURANTES_CATEGORIA)
    def __str__(self):
        return self.name

class Pedidos(models.Model):
    
    RESTAURANTES_PEDIDOS = (
        (1,"Sabor y punto"),
        (2,"Corralito"),
        (3,"Sabores y mixturas")
    )

    ESTADO_PEDIDOS = (
        (1,"Preparado"),
        (2,"Transportado"),
        (3,"Entregado")
    )

    producto = models.CharField(max_length=255)
    codigo = models.IntegerField(max_length=255)
    precio = models.IntegerField(max_length=255)
    cantidad = models.IntegerField(max_length=255)
    estado = models.IntegerField(max_length=1, choices=ESTADO_PEDIDOS)
    restaurantes = models.IntegerField(max_length=1, choices=RESTAURANTES_PEDIDOS)
    def __str__(self):
        return self.producto