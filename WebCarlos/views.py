from django.shortcuts import render
from django.http import HttpResponse
from .models import Motosierra, Desbrozadora, Cortacesped

# Create your views here.

def index(request):
        if request.method == "POST":
                return render (request, "enviado.html")
        else:
                return render (request, "index.html")

def motosierras(request):
        return render (request, "motosierras.html", {
                "motosierras": Motosierra.objects.all()
        })

def desbrozadoras(request):
        return render (request, "desbrozadoras.html", {
                "desbrozadoras": Desbrozadora.objects.all()
        })

def cortacespedes(request):
        return render (request, "cortacespedes.html", {
                "cortacespedes": Cortacesped.objects.all()
        })
