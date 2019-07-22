from django.shortcuts import render

# Create your views here.
def LinkedIn(request):
    return render(request, 'LinkedIn/LinkedIn.html')