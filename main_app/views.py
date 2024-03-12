from django.shortcuts import render
from .models import Planet

planet = Planet.objects.all()
herb= set()

for planet in planet:
    herbs = planet.herbs.split(', ')
    herb.update(herbs)

herb_list = sorted(list(herb))

body_systems = [
    {'system': 'Bladder', 'plants': 'plants'},
    {'system': 'Blood Tonic', 'plants': 'plants'},
    {'system': 'Brain and Nervous System', 'plants': 'plants'},
    {'system': 'Digestive', 'plants': 'plants'},
    {'system': 'Family Tonic', 'plants': 'plants'},
    {'system': 'First Aid', 'plants': 'plants'},
    {'system': 'Heart Health', 'plants': 'plants'},
    {'system': 'Lymphatic', 'plants': 'plants'},
    {'system': 'Men''s Health', 'plants': 'plants'},
    {'system': 'Musculoskeletal', 'plants': 'plants'},
    {'system': 'Respiratory', 'plants': 'plants'},
    {'system': 'Wellness/Immunity', 'plants': 'plants'},
    {'system': 'Women''s Health', 'plants': 'plants'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')
def planets_index(request):
    planet = Planet.objects.all()
    return render(request, 'planets/index.html', {'planet': planet})
def herbs_index(request):
    return render(request, 'herbs/index.html', {'herbs': herb_list})
def about(request):
    return render(request, 'about.html')
def bodysystems_index(request):
    return render(request, 'bodysystems/index.html', {'body_systems': body_systems})
def system(request, system):
    return render(request, 'bodysystems/system.html', {'system': system})
def herb(request, herb):
    return render(request, 'herbs/herb.html', {'herb': herb})