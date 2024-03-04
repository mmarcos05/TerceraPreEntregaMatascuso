from django import forms

#aca hago los formularios

class NewUser(forms.Form):
    username = forms.CharField(max_length = 15)
    password = forms.CharField(max_length = 20)
    conf_password = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 30)
    age = forms.IntegerField()
    country = forms.CharField(max_length = 30)