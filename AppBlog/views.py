from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from AppBlog.models import *
from AppBlog.forms import *




# Create your views here.

# LoGIN

def inicioSesion(request): 

    if request.method == "POST": #dando click al botón

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password=contra)

            if user: 

                login(request, user)

                return render(request, "AppBlog/inicio.html", {"mensaje":f"Hola {user}"})


        else: 

            return render(request, "AppBlog/inicio.html", {"mensaje": "Datos incorrectos."})

    else: # si no se le da click al botón

        form = AuthenticationForm()

    return render(request, "AppBlog/login.html", {"formulario":form})    

# Registro

def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppBlog/inicio.html", {"mensaje":"Usuario creado"})

    else: 

        form = UsuarioRegistro()

    return render(request, "AppBlog/registro.html", {"formulario": form})            


# modificar usuario
@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST) # hat que crearlo en forms 

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppBlog/inicio.html")

    else:

        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })        

    return render(request, "AppBlog/editarPerfil.html", {"formulario":form, "usuario":usuario})    






def inicio(request):
    #return HttpResponse("vista inicio")
    return render(request, "AppBlog/inicio.html")
    #avatares = Avatar.objects.filter(user=request.user.id)

    #contexto = {"url":avatares[0].imagen.url}

    #return render(request, "AppBlog/inicio.html", contexto)

def about(request):

    return render(request, "AppBlog/about.html")


def semillas(request):
    #return HttpResponse("vista semillas")
    return render(request, "AppBlog/semillas.html")

def plantas(request):
    #return HttpResponse("vista plantas")
    return render(request, "AppBlog/plantas.html")

def macetas(request):
    #return HttpResponse("vista macetas")
    return render(request, "AppBlog/macetas.html")

# Vistas de FORMULARIOS

def semillaFormulario(request):

    if request.method == "POST": # después de dar click al botón enviar

        formulario1 = SemillaFormulario(request.POST)

        #semilla = Semillas(nombre=request.POST["semilla"])

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            semilla = Semillas(nombre=info["nombre"])

            semilla.save()

            return render(request,"AppBlog/inicio.html") 

    else:     

        formulario1 = SemillaFormulario()

    return render(request,"AppBlog/semillaFormulario.html", {"form1":formulario1})

def macetaFormulario(request):

    if request.method == "POST":

        formulario2 = MacetaFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            maceta = Macetas (nombre=info["nombre"], modelo=info["modelo"])

            maceta.save()

            return render(request,"AppBlog/inicio.html")

    else:     

        formulario2 = MacetaFormulario()

    return render(request,"AppBlog/macetaFormulario.html", {"form2":formulario2})



def plantaFormulario(request):

    if request.method == "POST": # después de dar click al botón enviar

        formulario3 = PlantaFormulario(request.POST)

        #semilla = Semillas(nombre=request.POST["semilla"])

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            planta = Plantas(nombre=info["nombre"])

            planta.save()

            return render(request,"AppBlog/inicio.html") 

    else:     

        formulario3 = PlantaFormulario()

    return render(request,"AppBlog/plantaFormulario.html", {"form3":formulario3})







# Vistas de BUSCAR
#buscar semilla
def busquedanombresemilla(request): #vista para buscar

    return render (request, "AppBlog/inicio.html") # cambiar a inicio.html

def buscar(request): #vista para mostrar los resultados

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        semillas = Semillas.objects.filter(nombre__iexact=nombre) #

        return render(request, "AppBlog/inicio.html", {"semillas":semillas, "nombre":nombre}) #

    else: #

        respuesta = "No enviaste datos." #

    return HttpResponse(respuesta)    

    #return HttpResponse(f"Estás buscando el nombre de la semilla: {request.GET['nombre']}")  


#buscar planta
def busquedanombreplanta(request): #vista para buscar

    return render (request, "AppBlog/inicio.html") # cambiar a inicio.html

def buscarplanta(request): #vista para mostrar los resultados

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        plantas = Plantas.objects.filter(nombre__icontains=nombre)

        return render(request, "AppBlog/inicio.html", {"plantas":plantas, "nombre":nombre}) 
    else: 

        respuesta = "no enviaste datos."

    return HttpResponse(respuesta)    


    ##return HttpResponse(f"Estás buscando el nombre de la planta: {request.GET['nombre']}")  

##if request.GET["modelo"]:

#        modelo = request.GET["modelo"]
#        macetas = Macetas.objects.filter(modelo__iexact=modelo)

#        return render(request,"AppBlog/inicio.html", {"macetas":macetas, "modelo":modelo})

#    else: 

#        respuesta = "No enviaste datos."    

#    return HttpResponse(respuesta)

#buscar maceta
def busquedamodelomaceta(request):

    return render (request, "AppBlog/inicio.html") 

def buscarmodelo(request): #vista para mostrar los resultados

    if request.GET["modelo"]:

        modelo = request.GET["modelo"]
        macetas = Macetas.objects.filter(modelo__icontains=modelo)

        return render(request,"AppBlog/inicio.html", {"macetas":macetas, "modelo":modelo})

    else: 

        respuesta = "No enviaste datos."    

    return HttpResponse(respuesta) 
    
      
# Vistas de LEER
# leer macetas
@login_required
def leerMacetas(request):

    macetas = Macetas.objects.all()

    contexto = {"material": macetas} #variable contexto

    return render(request, "AppBlog/leerMacetas.html", contexto)
@login_required
def leerSemillas(request):

    semillas = Semillas.objects.all()

    contexto = {"tipo": semillas}

    return render(request, "AppBlog/leerSemillas.html", contexto)    

@login_required
def leerPlantas(request):

    plantas = Plantas.objects.all()

    contexto = {"especie": plantas}

    return render(request, "AppBlog/leerPlantas.html", contexto)

# Vistas de CREAR

def crearMacetas(request):

    if request.method == "POST":

        formulario2 = MacetaFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            maceta = Macetas (nombre=info["nombre"], modelo=info["modelo"])

            maceta.save()

            return render(request,"AppBlog/inicio.html")

    else:     

        formulario2 = MacetaFormulario()

    return render(request,"AppBlog/macetaFormulario.html", {"form2":formulario2})


def crearSemillas(request):

    if request.method == "POST": # después de dar click al botón enviar

        formulario1 = SemillaFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            semilla = Semillas(nombre=info["nombre"])

            semilla.save()

            return render(request,"AppBlog/inicio.html") 

    else:     

        formulario1 = SemillaFormulario()

    return render(request,"AppBlog/semillaFormulario.html", {"form1":formulario1})

def crearPlantas(request):

    if request.method == "POST": # después de dar click al botón enviar

        formulario3 = PlantaFormulario(request.POST)

        #semilla = Semillas(nombre=request.POST["semilla"])

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            planta = Plantas(nombre=info["nombre"])

            planta.save()

            return render(request,"AppBlog/inicio.html") 

    else:     

        formulario3 = PlantaFormulario()

    return render(request,"AppBlog/plantaFormulario.html", {"form3":formulario3})

# Vistas de ELIMINAR

def eliminarMacetas(request, macetaNombre):

    maceta = Macetas.objects.get(nombre=macetaNombre) #obtengo el nombre de la maceta indicada
    maceta.delete() # borro ese nombre de maceta

    macetas = Macetas.objects.all()  # mostrar todas las macetas

    contexto = {"material":macetas}

    return render(request, "AppBlog/leerMacetas.html", contexto)

def eliminarSemillas(request, semillaNombre):

    semilla = Semillas.objects.get(nombre=semillaNombre)
    semilla.delete()

    semillas = Semillas.objects.all()

    contexto = {"tipo":semillas}

    return render(request, "AppBlog/leerSemillas.html", contexto)     

def eliminarPlantas(request, plantaNombre):

    planta = Plantas.objects.get(nombre=plantaNombre)
    planta.delete()

    plantas = Plantas.objects.all()

    contexto = {"especie":plantas}

    return render(request, "AppBlog/leerPlantas.html", contexto)

# Vistas de EDITAR

def editarMacetas(request, macetaNombre):

    macetas = Macetas.objects.get(nombre=macetaNombre)

    if request.method == "POST":

        formulario2 = MacetaFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            macetas.nombre = info["nombre"]
            macetas.modelo = info["modelo"]

            macetas.save()

            return render(request,"AppBlog/inicio.html")

    else:     

        formulario2 = MacetaFormulario(initial={"nombre":macetas.nombre,"modelo":macetas.modelo}) # no mostrar formulario vacío 


    return render(request,"AppBlog/editarMaceta.html", {"form2":formulario2, "nombre":macetaNombre})


def editarSemillas(request, semillaNombre):

    semilla = Semillas.objects.get(nombre=semillaNombre)

    if request.method == "POST": 

        formulario1 = SemillaFormulario(request.POST)

        
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            semilla.nombre = info["nombre"]
            
            semilla.save()

            return render(request,"AppBlog/inicio.html") 

    else:     

        formulario1 = SemillaFormulario(initial={"nombre":semilla.nombre})

    return render(request,"AppBlog/editarSemilla.html", {"form1":formulario1, "nombre":semillaNombre})

def editarPlantas(request, plantaNombre):

    planta = Plantas.objects.get(nombre=plantaNombre)
    
    if request.method == "POST": 

        formulario3 = PlantaFormulario(request.POST)

        
        if formulario3.is_valid():

            info = formulario3.cleaned_data

            planta.nombre = info["nombre"]
            
            planta.save()

            return render(request,"AppBlog/inicio.html") 

    else:     

        formulario3 = PlantaFormulario(initial={"nombre":planta.nombre})

    return render(request,"AppBlog/editarPlanta.html", {"form3":formulario3, "nombre":plantaNombre})


# CRUD Vistas con clases
# Imágenes

@login_required
def agregarAvatar(request):

    if request.method=="POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user) # el usuario actual

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppBlog/inicio.html")

    else: 

        form = AvatarFormulario()

    return render(request, "AppBlog/agregarAvatar.html", {"formulario":form})            




# Semillas

class ListaSemilla(ListView):

    model = Semillas 

class DetalleSemilla(DetailView):

    model = Semillas

class CrearSemilla(CreateView):

    model = Semillas
    sucess_url = "/AppBlog/semillas/list"
    fields = ["nombre"] # en maceta agregar modelo

class ActualizarSemilla(UpdateView):

    model = Semillas
    sucess_url = "/AppBlog/semillas/list"
    fields = ["nombre"] # en maceta agregar modelo

class BorrarSemilla(DeleteView):

    model = Semillas
    sucess_url = "/AppBlog/semillas/list"


# Plantas

class ListaPlanta(ListView):

    model = Plantas
    

class DetallePlanta(DetailView):

    model = Plantas
    

class CrearPlanta(CreateView):

    model = Plantas
    success_url = "/AppBlog/plantas/list"
    fields = ['nombre']    

class ActualizarPlanta(UpdateView):

    model = Plantas
    sucess_url = "/AppBlog/plantas/list"
    fields = ['nombre']

class BorrarPlanta(DeleteView):

    model = Plantas
    sucess_url = "/AppBlog/plantas/list"

# Macetas
 
class ListaMaceta(ListView):

    model = Macetas

class DetalleMaceta(DetailView):

    model = Macetas

class CrearMaceta(CreateView):

    model = Macetas
    success_url = "/AppBlog/macetas/list"
    fields = ['nombre', 'modelo']    

class ActualizarMaceta(UpdateView):

    model = Macetas
    sucess_url = "/AppBlog/macetas/list"
    fields = ['nombre', 'modelo']

class BorrarMaceta(DeleteView):

    model = Macetas
    sucess_url = "/AppBlog/macetas/list"    







































# funciones de prueba

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
