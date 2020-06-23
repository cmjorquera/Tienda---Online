from django.shortcuts import render
from django.http import HttpResponse


# from django.http import HttpResponse
# import datetime 
# from datetime import date
# from django.template import Template, Context  # importar clase TEMPLATE y CONTEXT
# from django.template.loader import get_template  #importando el cargado de plantillas LOADER  
# from django.shortcuts import render # importar paquete /SIMPLIFICA EL VIDEO 8



# Create your views here.


def producto(request):
    return render(request,'busqueda_producto.html')
    
    
