from django.contrib import admin
from .models import Motosierra, Desbrozadora, Cortacesped

# Register your models here.
admin.site.register(Motosierra)
admin.site.register(Desbrozadora)
admin.site.register(Cortacesped)
