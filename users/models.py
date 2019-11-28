from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class InformationUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    briday_date = models.DateField()
    imagen = models.ImageField(verbose_name="Imagen", upload_to="Users")
   
    def __str__(self):
        return self.user.first_name