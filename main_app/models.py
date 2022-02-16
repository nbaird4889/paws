from django.db import models
from django.forms import DateField
from django.urls import reverse

# Create your models here.
class Walker(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Working On:')

    def __str__(self):
        return f"Walker is {self.name}"

class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=50)
    age = models.IntegerField()
    image = models.CharField(max_length=300)
    walker = models.ManyToManyField(Walker)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

class Visitors(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('visiting Date')

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} is visiting on {self.date}"


class Photo(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for dog_id: {self.dog_id} @ {self.url}"   
