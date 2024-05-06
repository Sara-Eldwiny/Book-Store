from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class new_book(models.Model):
    name=models.CharField(max_length=100, null=True)
    author=models.CharField(max_length=100, null=True, unique=True )
   # image=models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="bookstore/images/",null=True)
    pages=models.IntegerField(default=1000, null=True)
    price = models.IntegerField(default=700, null=True, validators=[MinValueValidator(700), MaxValueValidator(1000)])   
    creared_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return f"{self.name}"
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="authors/images/", null=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.name