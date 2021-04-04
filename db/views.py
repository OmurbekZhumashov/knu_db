from django.shortcuts import render
from .models import *


# Create your views here.
def home_view(request):
    qs = People.objects.all()

