from django.contrib import admin


# Register your models here.
from webapp.models import *
admin.site.register(Persona)
admin.site.register(Domicilio)
