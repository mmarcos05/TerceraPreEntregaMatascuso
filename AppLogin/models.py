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
    


