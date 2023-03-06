from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("enviado", views.index, name="enviado"),
        path("motosierras", views.motosierras, name="motosierras"),
	path("desbrozadoras", views.desbrozadoras, name="desbrozadoras"),
	path("cortacespedes", views.cortacespedes, name="cortacespedes"),
]
