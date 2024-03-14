from django.db import models

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=10)
    energies = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    other_ingredients = models.TextField(max_length=300)
    instructions = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class Herb(models.Model):
    name = models.CharField(max_length=50)
    planets = models.ManyToManyField(Planet, related_name='herbs')
    recipe_name = models.ManyToManyField(Recipe, related_name='herbs')
    
    def __str__(self):
        return self.name
