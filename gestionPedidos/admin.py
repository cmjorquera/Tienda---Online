from django.contrib import admin
from gestionPedidos.models import Clientes,Articulos, Pedidos, Ciudades,Peliculas1,Peliculas,xxx,ejemplo # importar la tabla Clientes


class Admin(admin.ModelAdmin):       ## logro poner estos parametros en el ADMIN
    list_display   =("nombre","direccion","telefono","email")  # muestras als COLUMNAS
    search_fields  =("nombre",)                                # COLUMNA que se buscara
    list_filter    =('nombre','direccion','telefono','email',)                    # filtro en el costado DERECHO
    ordering       =('-telefono',) # orden en que aparezcan als COLUMNAS

class AdminPedidos(admin.ModelAdmin):
    list_display  =("numero","entrega","fecha")   
    list_filter   =("fecha"), # filtro a la derecha POR FECHA     
    date_hierarchy = "fecha"    # filtro por meses  

# Register your models here.
# CREA LAS TABLAS EN LE PANEL DE DJANGO
admin.site.register(Clientes,Admin) 
admin.site.register(Articulos) 
admin.site.register(Pedidos, AdminPedidos)
admin.site.register(Ciudades) 
admin.site.register(Peliculas) 
admin.site.register(Peliculas1) 
admin.site.register(xxx) 
admin.site.register(ejemplo) 

