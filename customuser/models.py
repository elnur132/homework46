from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CreateUser(AbstractUser):
    phone = models.CharField(max_length=12)
    avatar = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.first_name, ' ', self.last_name