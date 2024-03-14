from django.db import models

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=10)
    herbs = models.TextField(max_length=300)
    energies = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=300)
    instructions = models.TextField(max_length=500)