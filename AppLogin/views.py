from django.shortcuts import render
from django.http import HttpResponse
from AppLogin.models import *
from django.shortcuts import render
from AppLogin.forms import *

# Create your views here.

def register(request):
    
    if request.method == "POST": #importante para verificar que haya confirmado el formulario
        
        form = NewUser(request.POST) #creamos un formulario
        
        if form.is_valid(): #chequeamos que sea valido
            
            info_dic = form.cleaned_data #convierte la info a un diccionario de python
            
            new_user = User(
                username=info_dic["username"],
                password=info_dic["password"],
                conf_password=info_dic["conf_password"],
                email=info_dic["email"],
                age = info_dic["age"],
                country = info_dic["country"]
                )
            
            new_user.save()
            
            return render(request, "complete_register.html") #aca ponemos a que pagina queremos que nos lleve
        
    else:
        
        formulario = NewUser
    
    return render(request, "register.html", {"formu":formulario})

def complete_register(request):
    
    return render(request, "complete_register")

def index(request):
    
    return render(request, "inicio.html")

def login(request):
    
    return render(request, "login.html")
