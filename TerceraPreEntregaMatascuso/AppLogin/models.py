from django.db import models

# Create your models here.

class User(models.Model):
    
    username = models.CharField(max_length = 15)
    password = models.CharField(max_length = 20)
    conf_password = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    age = models.IntegerField()
    country = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.username
    
class Help(models.Model):
    title = models.CharField(max_length = 15)
    text = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.title
    
class FootballShirt(models.Model):
    club_country = models.CharField(max_length = 25)
    year = models.IntegerField()
    short_sleeve = models.BooleanField()
    status = models.BooleanField()
    player = models.CharField(max_length = 30)
    number = models.IntegerField()
    price = models.IntegerField()
    
    
    


