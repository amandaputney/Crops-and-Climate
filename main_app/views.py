import uuid
import boto3
import os #access env vars
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
#import decorators
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

# Import the Model
from .models import Crop, Impact, Photo
#import form
from .forms import ReadingForm


# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

#for all users seeing all crops
# def crops_index(request):
#   crops = Crop.objects.all()
#   # We pass data to a template very much like we did in Express!
#   return render(request, 'crops/index.html', {
#     'crops': crops
#   })

#for user seeing only crops they created
@login_required
def crops_index(request):
  crops = Crop.objects.filter(user=request.user)
  # We pass data to a template very much like we did in Express!
  return render(request, 'crops/index.html', {
    'crops': crops
  })


@login_required
def crops_detail(request, crop_id):
  crop = Crop.objects.get(id=crop_id)
    #list of crop impact does have
  id_list = crop.impacts.all().values_list('id')

#query for the impacts that the crop doesn't have
#by using the exclude method vs the filter method
  impacts_crop_doesnt_have = Impact.objects.exclude(id__in=id_list)

  #instantiate reading form to be rendered in html
  reading_form = ReadingForm()
  return render(request, 'crops/detail.html', {
    'crop': crop, 'reading_form': reading_form,
    'impacts': impacts_crop_doesnt_have
    })


class CropCreate(LoginRequiredMixin, CreateView):
  model = Crop
  fields =  ['name', 'scientific_name', 'classification', 'regions', 'yields', 'acreage_of_production', 'description']

  def form_valid(self, form):
    #form.instance represents unsaved crop instance and self.request.user
    #represents logged in user
    form.instance.user = self.request.user
    #let the createview's form_valid method do its regular work
    #of saving object and reedirecting
    return super().form_valid(form)



class CropUpdate(LoginRequiredMixin, UpdateView):
  model = Crop
  fields = '__all__'



class CropDelete(LoginRequiredMixin, DeleteView):
  model = Crop
  success_url = '/crops'

@login_required
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


class ImpactCreate(LoginRequiredMixin, CreateView):
  model = Impact
  fields = '__all__'


class ImpactUpdate(LoginRequiredMixin, UpdateView):
  model = Impact
  fields = '__all__'


class ImpactDelete(LoginRequiredMixin, DeleteView):
  model = Impact
  success_url = '/impacts'

@login_required
def assoc_impact(request, crop_id, impact_id):
  Crop.objects.get(id=crop_id).impacts.add(impact_id)
  return redirect('detail', crop_id=crop_id)

@login_required
def unassoc_impact(request, crop_id, impact_id):
  Crop.objects.get(id=crop_id).impacts.remove(impact_id)
  return redirect('detail', crop_id=crop_id)

@login_required
def add_photo(request, crop_id):
  #photo file maps to name attribute on the <input>
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    #need unique key with same file extension of the file that was upload i.e. .jpg
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
     bucket = os.environ['S3_BUCKET']
     s3.upload_fileobj(photo_file, bucket, key)
     url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
     Photo.objects.create(url=url, crop_id=crop_id)
    except Exception as e:
      print('An error occured uploading file to S3')
      print(e)
  return redirect('detail', crop_id=crop_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    #this is how we creat a 'user' form object
    form = UserCreationForm(request.POST)
    if form.is_valid():
      #save the user to the db
      user = form.save()
      #automatically log in the new user
      #using login function that we imported at the top
      login(request, user)
      return redirect('index')
    else:
      error_message = "Invalid sign up, please try again."
  #a bad POST or a GET request, render sign up template
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


