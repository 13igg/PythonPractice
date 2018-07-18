from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    #get job objects form database and make them useable by django
    jobs = Job.objects

    return render(request, 'home.html', {'jobs': jobs})