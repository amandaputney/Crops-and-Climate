from django.db import models
from django.urls import reverse

REGIONS = (
   ('G', 'Global'),
   ('AF', 'Africa'),
   ('AS', 'Asia'),
   ('CR', 'Caribbean'),
   ('CA', 'Central America'),
   ('EU', 'Europe'),
   ('NA', 'North America'),
   ('OC', 'Oceania'),
   ('SA', 'South America'),
   ('O', 'Other'),
)

# Create your models here.
class Crop(models.Model):
  name = models.CharField(max_length=100)
  scientific_name = models.CharField(max_length=100)
  classification = models.CharField(max_length=100)
  regions = models.CharField(max_length=100)
  yields = models.CharField(max_length=100)
  acreage_of_production = models.CharField(max_length=100)
  description= models.TextField(max_length=999)

  def __str__(self):
    return f'{self.name} ({self.id})'
  
  def get_absolute_url(self):
      return reverse('detail', kwargs= {'crop_id':self.id})
  
class Reading(models.Model):
  date = models.DateField('Date Published')
  region = models.CharField(
     max_length=2,
     choices=REGIONS, 
        default='G'
  )
  author = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  source = models.CharField(max_length=200)
  crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE
        # this allows you to delete a crop with out any errors
    )
    
  def __str__(self):
    return f'{self.get_region_display()} on ({self.date})'
    
  class Meta:
    ordering = ['-date']
