from django.contrib import admin
from .models import Produto, Pedido, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    ...
admin.site.register(Produto, ProdutoAdmin)

class PedidoAdmin(admin.ModelAdmin):
    ...
admin.site.register(Pedido, PedidoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    ...
admin.site.register(Categoria, CategoriaAdmin)

# Register your models here.
