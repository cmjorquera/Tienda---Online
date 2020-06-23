from django.db import models

# Create your models here. 
# crear uan clase por casa tabla que necesite
#################################################################
#                   class xxx (model.Model)                     #
#################################################################

class Clientes (models.Model):
    nombre    = models.CharField(max_length=30, verbose_name= "El Nombre") 
    direccion = models.CharField(max_length=50,verbose_name= "La Direccion")     #verbose_name= 'La Direccion'
    email     = models.EmailField(blank= True, null= True, verbose_name = "El mail") # NO OBLIGATORIO
    telefono  = models.CharField(max_length=13, verbose_name = "El Telefono")

    def __str__(self):
        return self.nombre

class Articulos (models.Model):
    nombre  = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)   
    precio  = models.IntegerField() 

    def __str__ (self):
        return 'EL NOMBRE ES :  %s LA SECCION ES : %s EL PRECIO ES : %s' %(self.nombre, self.seccion,self.precio)

class Pedidos (models.Model):
    numero   = models.IntegerField()
    fecha    = models.DateField()
    entrega  = models.BooleanField()


class Ciudades (models.Model):
    nombre      = models.CharField(max_length=30)
    pais        = models.CharField(max_length=30)
    continente  = models.CharField(max_length=30)

class Peliculas1 (models.Model):
    nombre    = models.CharField(max_length=30) 
    edad      =  models.CharField(max_length=30) 

class Peliculas (models.Model):
    nombre    = models.CharField(max_length=30) 
    edad      = models.CharField(max_length=30) 

class xxx (models.Model):
    nombre    = models.CharField(max_length=30) 
    edad      = models.CharField(max_length=30) 

class ejemplo (models.Model):
    nombre    = models.CharField(max_length=30) 
    edad      = models.CharField(max_length=30) 
    
