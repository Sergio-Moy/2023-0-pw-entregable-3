from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Dish)
admin.site.register(models.Restaurant)
admin.site.register(models.Categorias)
admin.site.register(models.Pedidos)
admin.site.register(models.Plato)