from django.db import models

# Create your models here.
class Book() :
    author = models.CharField(max_lenght=50)
    title = models.CharField(max_length=70)
    

