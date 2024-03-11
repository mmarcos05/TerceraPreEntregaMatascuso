from django import forms

#aca hago los formularios

class NewUser(forms.Form):
    username = forms.CharField(max_length = 15)
    password = forms.CharField(max_length = 20)
    conf_password = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 30)
    age = forms.IntegerField()
    country = forms.CharField(max_length = 30)
    
class HelpMessage(forms.Form):
    title = forms.CharField(max_length = 15)
    text = forms.CharField(max_length = 300)
    
class FootballShirtForm(forms.Form):
    club_country = forms.CharField(max_length = 25)
    year = forms.IntegerField()
    short_sleeve = forms.BooleanField(required = False)
    status = forms.BooleanField(required = False)
    player = forms.CharField(max_length = 30)
    number = forms.IntegerField()
    price = forms.IntegerField()