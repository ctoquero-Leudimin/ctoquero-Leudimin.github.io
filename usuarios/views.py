from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def user(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	return render(request,"usuario.html")

def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username,password=password)

		if user:
			login(request,user)
			return HttpResponseRedirect(reverse("user"))
		else:
			render (request,"login.html", { "message": "Error, usuario o contraseña no válido"})
	return render(request,"login.html")

def logout_view(request):
	logout(request)
	return render(request, "login.html", { "message": "Ha cerrado sesión"})
