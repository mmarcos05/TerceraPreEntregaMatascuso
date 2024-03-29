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
        
        form = NewUser
    
    return render(request, "register.html", {"formu":form})

def complete_register(request):
    
    return render(request, "complete_register")

def index(request):
    
    return render(request, "inicio.html")

def login(request):
    
    return render(request, "login.html")

def contact(request):
    
    if request.method == "POST": #importante para verificar que haya confirmado el formulario
        
        form = HelpMessage(request.POST) #creamos un formulario
        
        if form.is_valid(): #chequeamos que sea valido
            
            info_dic = form.cleaned_data #convierte la info a un diccionario de python
            
            new_help = Help(
                title=info_dic["title"],
                text=info_dic["text"],

                )
            
            new_help.save()
            
            return render(request, "complete_help.html") #aca ponemos a que pagina queremos que nos lleve
        
    else:
        
        form = HelpMessage
    
    return render(request, "contact.html", {"formu":form})

def complete_help(request):
    
    return render(request, "complete_help.html")

def sell_shirt(request):
    
    if request.method == "POST": #importante para verificar que haya confirmado el formulario
        
        form = FootballShirtForm(request.POST) #creamos un formulario
        
        if form.is_valid(): #chequeamos que sea valido
            
            info_dic = form.cleaned_data #convierte la info a un diccionario de python
            
            new_shirt = FootballShirt(
                club_country=info_dic["club_country"],
                year=info_dic["year"],
                short_sleeve=info_dic["short_sleeve"],
                status=info_dic["status"],
                player = info_dic["player"],
                number = info_dic["number"],
                price = info_dic["price"]
                )
            
            new_shirt.save()
            
            return render(request, "complete_sell.html") #aca ponemos a que pagina queremos que nos lleve
        
    else:
        
        form = FootballShirtForm    
    
    return render(request, "sell_shirt.html", {"formu":form})

def complete_sell(request):
    
    return render(request, "complete_sell.html")

def search_offers(request):
    
    return render(request, "search_offers.html")
    
def offers_results(request):
    
    if request.GET["club_country"]:
        
        club_country = request.GET["club_country"]
        
        camisetas = FootballShirt.objects.filter(club_country__icontains = club_country)
        
        return render(request, "offers_results.html", {"camisetas" : camisetas, "club_country": club_country })
    
    else:
        
        respuesta = "No encontramos elementos que coincidan con su criterio de busqueda"
        
    return HttpResponse(respuesta)
    


