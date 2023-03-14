from django.shortcuts import render
from django.http import HttpResponse
from .models import Motosierra, Desbrozadora, Cortacesped
from .forms import Contacto

# Create your views here.

def index(request):
	if request.method == "POST":
		# No añado un método de validación ya que los navegadores modernos lo hacen por sí mismos
		return render (request, "enviado.html")
	else:
		form = Contacto()
		return render (request, "index.html", {'form': form})

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
