from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='gallery')
    overview = models.TextField()
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    
    def __str__(self):
        return self.name