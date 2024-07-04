from django.shortcuts import render
from .models import *
from .forms import *

def home(request):
    return render(request, "categorias/index.html")

def collares(request):
    contexto = {"collares": Collares.objects.all()}
    return render(request, "categorias/collares.html", contexto)

def alimentacion(request):
    contexto = {"alimentacion": Alimentacion.objects.all()}
    return render(request, "categorias/alimentacion.html", contexto)

def confort(request):
    contexto = {"confort": Confort.objects.all()}
    return render(request, "categorias/confort.html", contexto)

#Formularios

#Formulario para Collares

def collaresForm(request):
    if request.method == "POST":  
        miForm = CollaresForm(request.POST) 
        if miForm.is_valid():
            collar_tipo = miForm.cleaned_data.get("tipo") 
            collar_tamanio = miForm.cleaned_data.get("tamanio") 
            collar_precio = miForm.cleaned_data.get("precio")
            collar = Collares(tipo=collar_tipo, tamanio=collar_tamanio, precio=collar_precio) 
            collar.save()
            contexto = {"collares": Collares.objects.all()} 
            return render(request, "categorias/collares.html", contexto)
    else:
        miForm = CollaresForm()      
        
    return render(request, "categorias/collaresForm.html", {"form": miForm})

#Formulario para Alimentación

def alimentacionForm(request):
    if request.method == "POST":  
        miForm = AlimentacionForm(request.POST) 
        if miForm.is_valid():
            alimento_tipo = miForm.cleaned_data.get("tipo") 
            alimento_tamanio = miForm.cleaned_data.get("tamanio") 
            alimento_precio = miForm.cleaned_data.get("precio")
            alimento = Alimentacion(tipo=alimento_tipo, tamanio=alimento_tamanio, precio=alimento_precio) 
            alimento.save()
            contexto = {"alimentacion": Alimentacion.objects.all()} 
            return render(request, "categorias/alimentacion.html", contexto)
    else:
        miForm = AlimentacionForm()      
        
    return render(request, "categorias/alimentacionForm.html", {"form": miForm})

#Formulario para Confort

def confortForm(request):
    if request.method == "POST":  
        miForm = ConfortForm(request.POST) 
        if miForm.is_valid():
            confort_tipo = miForm.cleaned_data.get("tipo")  
            confort_precio = miForm.cleaned_data.get("precio")
            confort = Confort(tipo=confort_tipo, precio=confort_precio) 
            confort.save()
            contexto = {"confort": Confort.objects.all()} 
            return render(request, "categorias/confort.html", contexto)
    else:
        miForm = ConfortForm()      
        
    return render(request, "categorias/confortForm.html", {"form": miForm})

#Buscar en confort

def buscarConfort(request):
    return render(request, "categorias/buscar.html")

def encontrarConfort(request):
    if request.GET["buscar"]:  
        patron = request.GET["buscar"]
        confort = Confort.objects.filter(tipo__icontains=patron) 
        contexto = {'confort':confort}
    else:
        contexto = {'confort': Confort.objects.all()}
    
    return render(request,"categorias/confort.html", contexto)
