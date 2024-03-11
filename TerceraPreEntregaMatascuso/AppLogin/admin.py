from django.contrib import admin
from AppLogin.models import *

# Register your models here.

#agrego todos los modelos que voy a guardar en mi base de datos

admin.site.register(User)
admin.site.register(Help)
admin.site.register(FootballShirt)