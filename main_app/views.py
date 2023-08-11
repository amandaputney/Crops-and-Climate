from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Import the Model
from .models import Crop, Impact
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

    #list of crop impact does have
  id_list = crop.impacts.all().values_list('id')

#query for the impacts that the crop doesn't have
#by using the exclude method vs the filter method
  impacts_crop_doesnt_have = Crop.objects.exclude(id__in=id_list)

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
   

class ImpactList(ListView):
  model = Impact

class ImpactDetail(DetailView):
  model = Impact

class ImpactCreate(CreateView):
  model = Impact
  fields = '__all__'

class ImpactUpdate(UpdateView):
  model = Impact
  fields = '__all__'

class ImpactDelete(DeleteView):
  model = Impact
  success_url = '/impacts'

def assoc_impact(request, crop_id, impact_id):
  Crop.objects.get(id=crop_id).impacts.add(impact_id)
  return redirect('detail', crop_id=crop_id)

def unassoc_impact(request, crop_id, Impact_id):
  Crop.objects.get(id=crop_id).impacts.remove(impact_id)
  return redirect('detail', crop_id=crop_id)