from django.db import models
from django.urls import reverse

# Create your models here.
class Crop(models.Model):
  name = models.CharField(max_length=100)
  scientific_name = models.CharField(max_length=100)
  classification = models.CharField(max_length=100)
  regions= models.CharField(max_length=100)
  yields= models.CharField(max_length=100)
  acreage_of_production= models.IntegerField()
  description= models.TextField(max_length=350)

  def __str__(self):
    return f'{self.name} ({self.id})'
  
  def get_absolute_url(self):
      return reverse('detail', kwargs= {'crop_id':self.id})
