from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.name

