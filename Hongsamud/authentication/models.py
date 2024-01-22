from django.db import models
from django.contrib.auth.models import AbstractUser
from webpage.models import Book
# Create your models here.

class CustomUser(AbstractUser):
    
    #for borrow system
    Borrow=models.ManyToManyField(Book)
    