from django.urls import path
from AppLogin.views import *

urlpatterns = [
    path("", index, name = "Inicio"),
    
    path("login/", login, name = "Login"),
    
    path("register/", register, name = "Registro"),
    path("complete_register/", complete_register),
    
    path("contact.html/", contact, name = "Contact"),
    path("complete_help/", complete_help),
    
    path("sell_shirt/", sell_shirt, name = "Sell Shirt"),
    path("complete_sell/", complete_sell)   
]