from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'pics')
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Agency(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'agency_pics')
    description = models.TextField()

    def __str__(self):
        return self.name

