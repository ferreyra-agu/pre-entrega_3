from django.shortcuts import render
from django.http import HttpResponse
from hola_mundo.models import Tarea, Persona, Compras
from hola_mundo.forms import TareasForm, BuscarTareasForm, PersonaForm, BuscarPersonasForm, ComprasForm, BuscarComprasForm
from django.views.generic import ListView



def mostrar_mis_tareas(request):
    
    tareas = Tarea.objects.all()
    total_tareas = len(tareas)
    context = {
        "tareas": tareas, 
        "total_tareas":total_tareas,
        "form": TareasForm(),
    }
    return render(request, "hola_mundo/tareas.html", context)

def crear_tareas(request):

    f = TareasForm(request.POST)
    context = {
        "form": f
    } 
    if f.is_valid():
        Tarea(nombre=f.data["nombre"], estado=f.data["estado"], creado_el=f.data["creado_el"], modificado_el=f.data["modificado_el"]).save()
        context['form'] = TareasForm()

    context["tareas"] = Tarea.objects.all()
    context["total_tareas"] = len(Tarea.objects.all())
         
    return render(request, "hola_mundo/tareas.html", context)

class BuscarTareas(ListView):
    model = Tarea
    context_object_name = "tareas"

    def get_queryset(self):
        f = BuscarTareasForm(self.request.GET)
        if f.is_valid():
           return Tarea.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Tarea.objects.none()

def mostrar_personas(request):
    
    personas = Persona.objects.all()
    total_personas = len(personas)
    context = {
        "personas": personas, 
        "total_personas":total_personas,
        "form": PersonaForm(),
    }
    return render(request, "hola_mundo/personas.html", context)

def crear_persona(request):

    f = PersonaForm(request.POST)
    context = {
        "form": f
    } 
    if f.is_valid():
        Persona(nombre=f.data["nombre"], apellido=f.data["apellido"], fecha_nacimiento=f.data["fecha_nacimiento"]).save()
        context['form'] = PersonaForm()

    context["personas"] = Persona.objects.all()
    context["total_personas"] = len(Persona.objects.all())
         
    return render(request, "hola_mundo/personas.html", context)

class BuscarPersonas(ListView):
    model = Persona
    context_object_name = "personas"

    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
           return Persona.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Persona.objects.none()
    

def mostrar_compras(request):
    
    compras = Compras.objects.all()
    total_compras = len(compras)
    context = {
        "compras": compras, 
        "total_compras":total_compras,
        "form": ComprasForm(),
    }
    return render(request, "hola_mundo/compras.html", context)

def crear_compra(request):

    f = ComprasForm(request.POST)
    context = {
        "form": f
    } 
    if f.is_valid():
        Compras(articulo=f.data["articulo"], precio=f.data["precio"], fecha_de_compra=f.data["fecha_de_compra"]).save()
        context['form'] = ComprasForm()

    context["compras"] = Compras.objects.all()
    context["total_compras"] = len(Compras.objects.all())
         
    return render(request, "hola_mundo/compras.html", context)

class BuscarCompras(ListView):
    model = Compras
    context_object_name = "compras"

    def get_queryset(self):
        f = BuscarComprasForm(self.request.GET)
        if f.is_valid():
            return Compras.objects.filter(articulo__icontains=f.data["criterio_articulo"]).all()
        return Compras.objects.none()