from django.db import models

# Create your models here.


class CategoriaRestaurante(models.Model):
    categoría = models.CharField(max_length=255)

    def __str__(self):
        return self.categoría

class Restaurante(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaRestaurante, on_delete=models.CASCADE)
    imagen = models.URLField(max_length = 300)
    estado = models.CharField(
        max_length=1,
        choices=(
            ('1', 'Abierto'),
            ('0', 'Cerrado')
        ),
        default=1
    )
    def __str__(self):
        return self.nombre

class CategoriaPlato(models.Model):
    nombre = models.CharField(max_length=255)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class Oferta(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    descripción = models.TextField()
    imagen = models.URLField(max_length = 300)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    categoría = models.ForeignKey(CategoriaPlato, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class MostrarPlato(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    categoría = models.ForeignKey(CategoriaPlato, on_delete=models.CASCADE)
    producto = models.CharField(max_length=255)
    imagen = models.URLField(max_length=300)
    precio = models.FloatField()
    
    def __str__(self):
        return self.producto

class clienteulima(models.Model):
    codigo = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class PlatoRegistrado(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.PositiveSmallIntegerField()
    precio = models.FloatField()
    categoría = models.ForeignKey(CategoriaPlato, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    cliente = models.ForeignKey(clienteulima, on_delete=models.CASCADE)
    codigo_verificación = models.CharField(max_length=10)
    estado = models.CharField(
        max_length=20,
        choices=(
            ('1', 'Confirmado'),
            ('2', 'En preparación'),
            ('3', 'Entregado')
        )
    )
    registrado = models.CharField(
        max_length=3,
        choices=(
            ('1', 'Si'),
            ('2', 'No')
        )
    )
    def __str__(self):
        return self.producto

class Recomendacion(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.URLField(max_length=300)
    texto = models.TextField()

    def __str__(self):
        return self.nombre