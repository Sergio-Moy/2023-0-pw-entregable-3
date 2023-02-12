from django.db import models

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.CharField(max_length=30)
    
class Cliente(models.Model):
    codigo = models.CharField(max_length=8)
    password= models.CharField(max_length=50)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=50)
    carrera = models.CharField(max_length=50)
    
    def __str__(self):
        return self.codigo

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


class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    restaurante = models.ForeignKey(Restaurant,blank=True, on_delete=models.CASCADE)

    
class ofertas(models.Model):
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    restaurante = models.ForeignKey(Restaurant,blank=True, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    
    def __str__(self):
        return self.codigo
    

class CategoriaPlato(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class CategoriaRestaurante(models.Model):
    categoría = models.CharField(max_length=255)

    def __str__(self):
        return self.categoría

class Restaurante(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    categoría = models.ForeignKey(CategoriaRestaurante, on_delete=models.CASCADE)
    imagen = models.URLField(max_length = 300)
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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
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
        
class Pedidos(models.Model):

    producto = models.CharField(max_length=255)
    codigo = models.IntegerField(max_length=255)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField(max_length=255)
    estado = models.CharField(
        max_length=20,
        choices=(
            ('1', 'Confirmado'),
            ('2', 'En preparación'),
            ('3', 'Entregado')
        )
    )
    restaurantes = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    def __str__(self):
        return self.producto