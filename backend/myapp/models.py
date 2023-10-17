from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50,blank=False)
    name = models.CharField(max_length=50,blank=False)
    email = models.CharField(max_length=100,unique=True,blank=False)
    phone = models.PositiveIntegerField(max_length=10,unique=True)
    password = models.CharField(max_length=50)
    image = models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return f"{self.name} {self.id}"

