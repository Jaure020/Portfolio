from django.shortcuts import render
from .models import ecSeg

# Create your views here.
def ecSeg(request):
    return render(request, 'ecSeg/ecSeg.html', {'ecSeg':ecSeg})
