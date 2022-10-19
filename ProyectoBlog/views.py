from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader


from AppBlog.models import *

#from AppBlog.forms import * 

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



def saludo(request):

    return HttpResponse("Hola Mundo!")

def hoy(request):

    fecha = datetime.now()

    return HttpResponse(f"El día de hoy es {fecha}.") 

def name(request, nombre):

    return HttpResponse(f"Tu nombre es: {nombre}")     

def prueba(request):

    nom = "Carla"
    listaDeNotas = [10,10,10,10,10]

    diccionario = {"nombre":nom, "notas":listaDeNotas} # envia al contexto

    #miHtml = open("C:/Users/Carla Albornoz/Desktop/ProyectoFinal/ProyectoBlog/ProyectoBlog/plantillas/plantilla1.html")    

    #plantilla = Template(miHtml.read())

    #miHtml.close()

    #miContexto = Context(diccionario)

    #documento = plantilla.render(miContexto) 

    plantilla = loader.get_template('plantilla1.html')

    documento = plantilla.render(diccionario) # no se necesita más un contexto, usamos el diccionario
    
    return HttpResponse(documento)


def semillas(request): # segunda prueba

    sem1 = Semillas(nombre="Espinaca")
    sem1.save()

    return HttpResponse(f"La semilla que se ha guardado es: {sem1.nombre}.")

#def semillas(self): # primera prueba 

    #sem1 = Semillas(nombre="Sésamo")
    #sem1.save()
    #documentoDeTexto = f"--->Semilla:{sem1.nombre}"
    #return HttpResponse(documentoDeTexto)    

#def semillas(request): # tercera prueba, esta función es la que vale 
   #sem1 = Semillas(nombre="Espinaca") 

   #sem1.save()

   #sem2 = Semillas(nombre="Cebolla")
   #sem2.save()

   #sem3 = Semillas(nombre="Remolacha")
   #sem3.save()

   #return render (request, "AppBlog/semillas.html")    

    