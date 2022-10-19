from django.urls import path
from AppBlog import views
from AppBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("about/", about, name="About"),
    path('semillas/', semillas, name="Semillas"),
    path("plantas/", plantas, name="Plantas"),
    path("macetas/", macetas, name="Macetas"),
    
    path("semillaFormulario/", semillaFormulario, name="FormularioSemilla"),
    path("buscarnombresemilla/", busquedanombresemilla, name="BuscarSemilla"),
    path("buscar/", buscar, name="ResultadosBusquedaSemilla"),

    path("macetaFormulario/", macetaFormulario, name="FormularioMaceta"),
    path("buscarmodelomaceta/", busquedamodelomaceta, name="BuscarModelo"),
    path("buscarmodelo/", buscarmodelo, name="ResultadoBusquedaMaceta"),

    path("plantaFormulario/", plantaFormulario, name="FormularioPlanta"),
    path("buscarnombreplanta/", busquedanombreplanta, name="BuscarPlanta"),
    path("buscarplanta/", buscarplanta, name="ResultadoBusquedaPlanta"),

    path("login/", inicioSesion, name="Login"),
    path("register/", registro, name="Registro"),
    path("logout/", LogoutView.as_view(template_name="AppBlog/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar/", agregarAvatar, name="Avatar"),
    

    #CRUD de Macetas
    path("leerMacetas/", leerMacetas, name="MacetasLeer"),
    path("crearMacetas/", crearMacetas, name="MacetasCrear"),
    path("eliminarMacetas/<macetaNombre>/", eliminarMacetas, name="MacetaEliminar"),
    path("editarMacetas/<macetaNombre>/", editarMacetas, name="MacetaEditar"),

    #CRUD de Semillas
    path("leerSemillas/", leerSemillas, name="SemillasLeer"),
    path("crearSemillas/", crearSemillas, name="SemillasCrear"),
    path("eliminarSemillas/<semillaNombre>/", eliminarSemillas, name="SemillaEliminar"),
    path("editarSemillas/<semillaNombre>/", editarSemillas, name="SemillaEditar"),

    #CRUD de Plantas
    path("leerPlantas/", leerPlantas, name="PlantasLeer"),
    path("crearPlantas/", crearPlantas, name="PlantasCrear"),
    path("eliminarPlantas/<plantaNombre>/", eliminarPlantas, name="PlantaEliminar"),
    path("editarPlantas/<plantaNombre>/", editarPlantas, name="PlantaEditar"),

    # CRUD de Semillas usando clases
    path("semillas/list/", ListaSemilla.as_view(), name="SemillasLeer"),
    path("semillas/<int:pk>", DetalleSemilla.as_view(), name="SemillasDetalle"),
    path("semillas/crear/", CrearSemilla.as_view(), name="SemillasCrear"),
    path("semillas/editar/<int:pk>", ActualizarSemilla.as_view(), name="SemillasEditar"),
    path("semillas/borrar/<int:pk>", BorrarSemilla.as_view(), name="SemillasBorrar"),

    # CRUD de Plantas usando clases
    path("plantas/list/", ListaPlanta.as_view(), name="PlantasLeer"),
    path("plantas/<int:pk>", DetallePlanta.as_view(), name="PlantasDetalle"),
    path("plantas/crear/", CrearPlanta.as_view(), name="PlantasCrear"),
    path("plantas/editar/<int:pk>", ActualizarPlanta.as_view(), name="PlantasEditar"),
    path("plantas/borrar/<int:pk>", BorrarPlanta.as_view(), name="PlantasBorrar"), 

    # CRUD  de Mactas usando clases
    path("macetas/list/", ListaMaceta.as_view(), name="MacetasLeer"),
    path("macetas/<int:pk>", DetalleMaceta.as_view(), name="MacetasDetalle"),
    path("macetas/crear/", CrearMaceta.as_view(), name="MacetasCrear"),
    path("macetas/editar/<int:pk>", ActualizarMaceta.as_view(), name="MacetasEditar"),
    path("macetas/borrar/<int:pk>", BorrarMaceta.as_view(), name="MacetasBorrar"),









    # urls de prueba
    path('saludo/', saludo),
    path('fechaHoy/', hoy),
    path('persona/<nombre>', name),
    path('probando/', prueba),
]
