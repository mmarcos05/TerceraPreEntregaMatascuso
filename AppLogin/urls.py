from django.urls import path
from AppLogin.views import *

urlpatterns = [
    path("register/", register, name = "Registro"),
    path("", index, name = "Inicio"),
    path("login/", login, name = "Login"),
    path("complete_register", complete_register)
    
    
    
]