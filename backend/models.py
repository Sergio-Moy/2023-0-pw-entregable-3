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