from django.shortcuts import render

crops= [
  {'name': 'Wheat', 'regions': 'North America', 'yields': 'increase', 'acreage of production': 540000000 },
  {'name': 'Rice', 'regions': 'North America', 'yields': 'increase', 'acreage of production': 540000000 },
  {'name': 'Banana', 'regions': 'North America', 'yields': 'increase', 'acreage of production': 540000000 },
]

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def crops_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'crops/index.html', {
    'crops': crops
  })