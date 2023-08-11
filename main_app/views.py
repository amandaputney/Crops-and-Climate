from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the Model
from .models import Crop
#import form
from .forms import ReadingForm
# crops= [
#   {'name': 'Wheat', 'regions': 'North America', 'yields': 'increase', 'acreage of production': 540000000 },
#   {'name': 'Rice', 'regions': 'North America', 'yields': 'increase', 'acreage of production': 540000000 },
#   {'name': 'Banana', 'regions': 'North America', 'yields': 'increase', 'acreage of production': 540000000 },
# ]

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def crops_index(request):
  crops = Crop.objects.all()
  # We pass data to a template very much like we did in Express!
  return render(request, 'crops/index.html', {
    'crops': crops
  })

def crops_detail(request, crop_id):
  crop = Crop.objects.get(id=crop_id)
  #instantiate reading form to be rendered in html
  reading_form = ReadingForm()
  return render(request, 'crops/detail.html', {
    'crop': crop, 'reading_form': reading_form
    })

class CropCreate(CreateView):
  model = Crop
  fields = '__all__'

class CropUpdate(UpdateView):
  model = Crop
  fields = '__all__'

class CropDelete(DeleteView):
  model = Crop
  success_url = '/crops'

def add_reading(request, crop_id):
   #create a ModelForm instance using submitted form data 
   form = ReadingForm(request.POST)
   #validate form
   if form.is_valid():
      #we want a model instance but we can't save to the db yet
      #because we have not assign a crop_id FK
      new_reading = form.save(commit=False)
      new_reading.crop_id = crop_id
      new_reading.save()
      return redirect('detail',crop_id=crop_id) 
   